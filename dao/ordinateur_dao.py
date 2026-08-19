from database.connexion import get_connexion
from models.ordinateur import Ordinateur
from models.intervention import Intervention


# ---------- ORDINATEURS ----------

def ajouter_ordinateur(code, marque, modele, etat, salle_id):
    """Ajoute un nouvel ordinateur et retourne son id."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "INSERT INTO ordinateur (code, marque, modele, etat, salle_id) VALUES (?, ?, ?, ?, ?)",
        (code, marque, modele, etat, salle_id)
    )
    connexion.commit()
    nouvel_id = curseur.lastrowid
    connexion.close()
    return nouvel_id


def lister_ordinateurs():
    """Retourne la liste de tous les ordinateurs."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, code, marque, modele, etat, salle_id, date_creation FROM ordinateur")
    lignes = curseur.fetchall()
    connexion.close()

    ordinateurs = []
    for ligne in lignes:
        ordinateurs.append(Ordinateur(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6]))
    return ordinateurs


def lister_ordinateurs_par_salle(salle_id):
    """Retourne les ordinateurs d'une salle donnée."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, code, marque, modele, etat, salle_id, date_creation FROM ordinateur WHERE salle_id = ?",
        (salle_id,)
    )
    lignes = curseur.fetchall()
    connexion.close()

    ordinateurs = []
    for ligne in lignes:
        ordinateurs.append(Ordinateur(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6]))
    return ordinateurs


def get_ordinateur_par_id(ordinateur_id):
    """Retourne un ordinateur à partir de son id, ou None."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, code, marque, modele, etat, salle_id, date_creation FROM ordinateur WHERE id = ?",
        (ordinateur_id,)
    )
    ligne = curseur.fetchone()
    connexion.close()

    if ligne is None:
        return None
    return Ordinateur(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6])


def rechercher_par_code(code):
    """Recherche un ordinateur par son code (fonctionnalité bonus)."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, code, marque, modele, etat, salle_id, date_creation FROM ordinateur WHERE code = ?",
        (code,)
    )
    ligne = curseur.fetchone()
    connexion.close()

    if ligne is None:
        return None
    return Ordinateur(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6])


def modifier_ordinateur(ordinateur_id, marque, modele, etat, salle_id):
    """Modifie les informations d'un ordinateur (état, salle, etc.)."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "UPDATE ordinateur SET marque = ?, modele = ?, etat = ?, salle_id = ? WHERE id = ?",
        (marque, modele, etat, salle_id, ordinateur_id)
    )
    connexion.commit()
    lignes_modifiees = curseur.rowcount
    connexion.close()
    return lignes_modifiees > 0


def supprimer_ordinateur(ordinateur_id):
    """Supprime un ordinateur (les interventions liées sont supprimées automatiquement)."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM ordinateur WHERE id = ?", (ordinateur_id,))
    connexion.commit()
    lignes_supprimees = curseur.rowcount
    connexion.close()
    return lignes_supprimees > 0


def lister_ordinateurs_mauvais_etat():
    """Retourne les ordinateurs en état MAUVAIS ou HS."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, code, marque, modele, etat, salle_id, date_creation FROM ordinateur WHERE etat IN ('MAUVAIS', 'HS')"
    )
    lignes = curseur.fetchall()
    connexion.close()

    ordinateurs = []
    for ligne in lignes:
        ordinateurs.append(Ordinateur(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6]))
    return ordinateurs


def filtrer_par_marque(marque):
    """Retourne les ordinateurs d'une marque donnée (fonctionnalité bonus)."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, code, marque, modele, etat, salle_id, date_creation FROM ordinateur WHERE marque = ?",
        (marque,)
    )
    lignes = curseur.fetchall()
    connexion.close()

    ordinateurs = []
    for ligne in lignes:
        ordinateurs.append(Ordinateur(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6]))
    return ordinateurs


def statistiques_etats():
    """Retourne le nombre total d'ordinateurs et le nombre par état (fonctionnalité bonus)."""
    connexion = get_connexion()
    curseur = connexion.cursor()

    curseur.execute("SELECT COUNT(*) FROM ordinateur")
    total = curseur.fetchone()[0]

    curseur.execute("SELECT etat, COUNT(*) FROM ordinateur GROUP BY etat")
    par_etat = curseur.fetchall()

    connexion.close()
    return total, par_etat


# ---------- INTERVENTIONS ----------

def ajouter_intervention(ordinateur_id, description):
    """Ajoute une intervention sur un ordinateur."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "INSERT INTO intervention (ordinateur_id, description) VALUES (?, ?)",
        (ordinateur_id, description)
    )
    connexion.commit()
    nouvel_id = curseur.lastrowid
    connexion.close()
    return nouvel_id


def historique_interventions(ordinateur_id):
    """Retourne toutes les interventions faites sur un ordinateur donné."""
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute(
        "SELECT id, ordinateur_id, description, date_intervention FROM intervention WHERE ordinateur_id = ?",
        (ordinateur_id,)
    )
    lignes = curseur.fetchall()
    connexion.close()

    interventions = []
    for ligne in lignes:
        interventions.append(Intervention(ligne[0], ligne[1], ligne[2], ligne[3]))
    return interventions
