from database.connexion import get_connexion
from models.salle import Salle


def ajouter_salle(nom, capacite, batiment):
   
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "INSERT INTO salle (nom, capacite, batiment) VALUES (?, ?, ?)",
        (nom, capacite, batiment)
    )
    connexion.commit()
    nouvel_id = curseur.lastrowid
    connexion.close()
    return nouvel_id


def lister_salles():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, nom, capacite, batiment, date_creation FROM salle")
    lignes = curseur.fetchall()
    connexion.close()

    salles = []
    for ligne in lignes:
        salles.append(Salle(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4]))
    return salles


def get_salle_par_id(salle_id):
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, nom, capacite, batiment, date_creation FROM salle WHERE id = ?", (salle_id,))
    ligne = curseur.fetchone()
    connexion.close()

    if ligne is None:
        return None
    return Salle(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4])


def modifier_salle(salle_id, nom, capacite, batiment):
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "UPDATE salle SET nom = ?, capacite = ?, batiment = ? WHERE id = ?",
        (nom, capacite, batiment, salle_id)
    )
    connexion.commit()
    lignes_modifiees = curseur.rowcount
    connexion.close()
    return lignes_modifiees > 0


def supprimer_salle(salle_id):
    connexion = get_connexion()
    curseur = connexion.cursor()

    curseur.execute("SELECT COUNT(*) FROM ordinateur WHERE salle_id = ?", (salle_id,))
    nb_ordinateurs = curseur.fetchone()[0]

    if nb_ordinateurs > 0:
        connexion.close()
        return False

    curseur.execute("DELETE FROM salle WHERE id = ?", (salle_id,))
    connexion.commit()
    connexion.close()
    return True


def compter_ordinateurs_par_salle():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("""
        SELECT salle.nom, COUNT(ordinateur.id)
        FROM salle
        LEFT JOIN ordinateur ON ordinateur.salle_id = salle.id
        GROUP BY salle.id
    """)
    resultat = curseur.fetchall()
    connexion.close()
    return resultat


def lister_salles_par_batiment():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, nom, capacite, batiment, date_creation FROM salle ORDER BY batiment")
    lignes = curseur.fetchall()
    connexion.close()

    salles = []
    for ligne in lignes:
        salles.append(Salle(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4]))
    return salles
