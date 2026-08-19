from dao import salle_dao
from dao import ordinateur_dao
from models.ordinateur import ETATS_VALIDES


def menu_salles():
    while True:
        print("\n--- GESTION DES SALLES ---")
        print("1. Ajouter une salle")
        print("2. Afficher toutes les salles")
        print("3. Modifier une salle")
        print("4. Supprimer une salle")
        print("0. Retour")
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_salle()
        elif choix == "2":
            afficher_salles()
        elif choix == "3":
            modifier_salle()
        elif choix == "4":
            supprimer_salle()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")


def ajouter_salle():
    try:
        nom = input("Nom de la salle : ")
        capacite = int(input("Capacité : "))
        batiment = input("Bâtiment : ")

        salle_id = salle_dao.ajouter_salle(nom, capacite, batiment)
        print(f"Salle ajoutée avec succès (ID: {salle_id})")
    except ValueError:
        print("Erreur : la capacité doit être un nombre entier.")


def afficher_salles():
    salles = salle_dao.lister_salles()
    if not salles:
        print("Aucune salle enregistrée.")
        return
    print("\n--- Liste des salles ---")
    for salle in salles:
        print(salle)


def modifier_salle():
    try:
        salle_id = int(input("ID de la salle à modifier : "))
        salle = salle_dao.get_salle_par_id(salle_id)

        if salle is None:
            print("Aucune salle trouvée avec cet ID.")
            return

        print(f"Salle actuelle : {salle}")
        nom = input(f"Nouveau nom [{salle.nom}] : ") or salle.nom
        capacite_saisie = input(f"Nouvelle capacité [{salle.capacite}] : ")
        capacite = int(capacite_saisie) if capacite_saisie else salle.capacite
        batiment = input(f"Nouveau bâtiment [{salle.batiment}] : ") or salle.batiment

        if salle_dao.modifier_salle(salle_id, nom, capacite, batiment):
            print("Salle modifiée avec succès.")
        else:
            print("La modification a échoué.")
    except ValueError:
        print("Erreur : l'ID et la capacité doivent être des nombres entiers.")
    except Exception as e:
        print(f"Erreur lors de la modification : {e}")


def supprimer_salle():
    try:
        salle_id = int(input("ID de la salle à supprimer : "))
        if salle_dao.supprimer_salle(salle_id):
            print("Salle supprimée avec succès.")
        else:
            print("Impossible de supprimer cette salle : elle contient des ordinateurs, "
                  "ou elle n'existe pas.")
    except ValueError:
        print("Erreur : l'ID doit être un nombre entier.")


# ---------------------------------------------------------
# MENU ORDINATEURS
# ---------------------------------------------------------

def menu_ordinateurs():
    while True:
        print("\n--- GESTION DES ORDINATEURS ---")
        print("1. Ajouter un ordinateur")
        print("2. Afficher tous les ordinateurs")
        print("3. Afficher les ordinateurs par salle")
        print("4. Modifier un ordinateur")
        print("5. Supprimer un ordinateur")
        print("6. Rechercher un ordinateur par code")
        print("7. Filtrer les ordinateurs par marque")
        print("0. Retour")
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_ordinateur()
        elif choix == "2":
            afficher_ordinateurs()
        elif choix == "3":
            afficher_ordinateurs_par_salle()
        elif choix == "4":
            modifier_ordinateur()
        elif choix == "5":
            supprimer_ordinateur()
        elif choix == "6":
            rechercher_par_code()
        elif choix == "7":
            filtrer_par_marque()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")


def demander_etat():
    """Demande l'état à l'utilisateur et vérifie qu'il est valide."""
    etat = input("État (BON/MOYEN/MAUVAIS/HS) : ").upper()
    while etat not in ETATS_VALIDES:
        print(f"État invalide. Les valeurs autorisées sont : {', '.join(ETATS_VALIDES)}")
        etat = input("État (BON/MOYEN/MAUVAIS/HS) : ").upper()
    return etat


def ajouter_ordinateur():
    try:
        code = input("Code du PC : ")
        marque = input("Marque : ")
        modele = input("Modèle : ")
        etat = demander_etat()
        salle_id = int(input("ID de la salle : "))
        if salle_dao.get_salle_par_id(salle_id) is None:
            print("Erreur : cette salle n'existe pas.")
            return

        ordinateur_id = ordinateur_dao.ajouter_ordinateur(code, marque, modele, etat, salle_id)
        print(f"Ordinateur ajouté avec succès (ID: {ordinateur_id})")
    except ValueError:
        print("Erreur : l'ID de la salle doit être un nombre entier.")


def afficher_ordinateurs():
    ordinateurs = ordinateur_dao.lister_ordinateurs()
    if not ordinateurs:
        print("Aucun ordinateur enregistré.")
        return
    print("\n--- Liste des ordinateurs ---")
    for ordinateur in ordinateurs:
        print(ordinateur)


def afficher_ordinateurs_par_salle():
    try:
        salle_id = int(input("ID de la salle : "))
        ordinateurs = ordinateur_dao.lister_ordinateurs_par_salle(salle_id)
        if not ordinateurs:
            print("Aucun ordinateur dans cette salle.")
            return
        print(f"\n--- Ordinateurs de la salle {salle_id} ---")
        for ordinateur in ordinateurs:
            print(ordinateur)
    except ValueError:
        print("Erreur : l'ID doit être un nombre entier.")


def modifier_ordinateur():
    try:
        ordinateur_id = int(input("ID de l'ordinateur à modifier : "))
        ordinateur = ordinateur_dao.get_ordinateur_par_id(ordinateur_id)

        if ordinateur is None:
            print("Aucun ordinateur trouvé avec cet ID.")
            return

        print(f"Ordinateur actuel : {ordinateur}")
        marque = input(f"Nouvelle marque [{ordinateur.marque}] : ") or ordinateur.marque
        modele = input(f"Nouveau modèle [{ordinateur.modele}] : ") or ordinateur.modele
        etat = input(f"Nouvel état [{ordinateur.etat}] (laisser vide pour ne pas changer) : ").upper()
        if etat == "":
            etat = ordinateur.etat
        elif etat not in ETATS_VALIDES:
            print(f"État invalide. Les valeurs autorisées sont : {', '.join(ETATS_VALIDES)}")
            return

        salle_saisie = input(f"Nouvelle salle (ID) [{ordinateur.salle_id}] : ")
        salle_id = int(salle_saisie) if salle_saisie else ordinateur.salle_id

        if ordinateur_dao.modifier_ordinateur(ordinateur_id, marque, modele, etat, salle_id):
            print("Ordinateur modifié avec succès.")
        else:
            print("La modification a échoué.")
    except ValueError:
        print("Erreur : l'ID doit être des nombres entiers.")


def supprimer_ordinateur():
    try:
        ordinateur_id = int(input("ID de l'ordinateur à supprimer : "))
        if ordinateur_dao.supprimer_ordinateur(ordinateur_id):
            print("Ordinateur supprimé avec succès.")
        else:
            print("Aucun ordinateur trouvé avec cet ID.")
    except ValueError:
        print("Erreur : l'ID doit être un nombre entier.")


def rechercher_par_code():
    code = input("Code de l'ordinateur recherché : ")
    ordinateur = ordinateur_dao.rechercher_par_code(code)
    if ordinateur is None:
        print("Aucun ordinateur trouvé avec ce code.")
    else:
        print(f"Trouvé : {ordinateur}")


def filtrer_par_marque():
    marque = input("Marque recherchée : ")
    ordinateurs = ordinateur_dao.filtrer_par_marque(marque)
    if not ordinateurs:
        print("Aucun ordinateur de cette marque.")
        return
    print(f"\n--- Ordinateurs de marque {marque} ---")
    for ordinateur in ordinateurs:
        print(ordinateur)


def menu_interventions():
    while True:
        print("\n--- INTERVENTIONS ---")
        print("1. Signaler une intervention")
        print("2. Afficher l'historique des interventions d'un ordinateur")
        print("0. Retour")
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_intervention()
        elif choix == "2":
            afficher_historique()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")


def ajouter_intervention():
    try:
        ordinateur_id = int(input("ID de l'ordinateur concerné : "))
        if ordinateur_dao.get_ordinateur_par_id(ordinateur_id) is None:
            print("Erreur : cet ordinateur n'existe pas.")
            return
        description = input("Description de l'intervention : ")
        ordinateur_dao.ajouter_intervention(ordinateur_id, description)
        print("Intervention enregistrée avec succès.")
    except ValueError:
        print("Erreur : l'ID doit être un nombre entier.")


def afficher_historique():
    try:
        ordinateur_id = int(input("ID de l'ordinateur : "))
        interventions = ordinateur_dao.historique_interventions(ordinateur_id)
        if not interventions:
            print("Aucune intervention enregistrée pour cet ordinateur.")
            return
        print(f"\n--- Historique des interventions (ordinateur {ordinateur_id}) ---")
        for intervention in interventions:
            print(intervention)
    except ValueError:
        print("Erreur : l'ID doit être un nombre entier.")



def menu_rapports():
    while True:
        print("\n--- RAPPORTS ---")
        print("1. Nombre d'ordinateurs par salle")
        print("2. Ordinateurs en mauvais état (MAUVAIS ou HS)")
        print("3. Salles par bâtiment")
        print("4. Statistiques générales")
        print("0. Retour")
        choix = input("Votre choix : ")

        if choix == "1":
            rapport_ordinateurs_par_salle()
        elif choix == "2":
            rapport_mauvais_etat()
        elif choix == "3":
            rapport_salles_par_batiment()
        elif choix == "4":
            rapport_statistiques()
        elif choix == "0":
            break
        else:
            print("Choix invalide.")


def rapport_ordinateurs_par_salle():
    resultats = salle_dao.compter_ordinateurs_par_salle()
    print("\n--- Nombre d'ordinateurs par salle ---")
    for nom_salle, nb_ordinateurs in resultats:
        print(f"{nom_salle} : {nb_ordinateurs} ordinateur(s)")


def rapport_mauvais_etat():
    ordinateurs = ordinateur_dao.lister_ordinateurs_mauvais_etat()
    if not ordinateurs:
        print("Aucun ordinateur en mauvais état.")
        return
    print("\n--- Ordinateurs en mauvais état ---")
    for ordinateur in ordinateurs:
        print(ordinateur)


def rapport_salles_par_batiment():
    salles = salle_dao.lister_salles_par_batiment()
    print("\n--- Salles par bâtiment ---")
    for salle in salles:
        print(salle)


def rapport_statistiques():
    total, par_etat = ordinateur_dao.statistiques_etats()
    print(f"\n--- Statistiques ---")
    print(f"Nombre total d'ordinateurs : {total}")
    if total == 0:
        return
    for etat, nombre in par_etat:
        pourcentage = (nombre / total) * 100
        print(f"{etat} : {nombre} ({pourcentage:.1f}%)")

def menu_principal():
    while True:
        print("\n========================================")
        print("GESTION DES SALLES INFORMATIQUES")
        print("========================================")
        print("1. Gestion des salles")
        print("2. Gestion des ordinateurs")
        print("3. Interventions")
        print("4. Rapports")
        print("0. Quitter")
        print("----------------------------------------")
        choix = input("Votre choix : ")

        if choix == "1":
            menu_salles()
        elif choix == "2":
            menu_ordinateurs()
        elif choix == "3":
            menu_interventions()
        elif choix == "4":
            menu_rapports()
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
