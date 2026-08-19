# Gestion des Salles Informatiques

Projet de Programmation - POO & Base de données
Licence 2 - Réseaux Informatique

## Description

Application console en Python permettant à une école de gérer ses salles
informatiques et le matériel qu'elles contiennent :

- Gestion des salles (nom, capacité, bâtiment)
- Gestion des ordinateurs (marque, modèle, état) et de leur affectation à une salle
- Suivi des interventions techniques sur les ordinateurs
- Génération de rapports simples (nombre d'ordinateurs par salle, ordinateurs
  en mauvais état, salles par bâtiment, statistiques)

## Base de données

Le projet utilise **SQLite** (module `sqlite3` intégré à Python), ce qui évite
d'avoir à installer un serveur de base de données séparé. Le fichier
`gestion_salles.db` est créé automatiquement au premier lancement.

### Tables

- **salle** : id, nom, capacite, batiment, date_creation
- **ordinateur** : id, code, marque, modele, etat, salle_id, date_creation
- **intervention** : id, ordinateur_id, description, date_intervention

## Structure du projet

```
gestion_salles/
    database/
        config.py       # Configuration de la base de données
        connexion.py     # Connexion à la base de données
    models/
        salle.py         # Classe Salle
        ordinateur.py     # Classe Ordinateur
        intervention.py   # Classe Intervention
    dao/
        salle_dao.py      # Opérations CRUD sur les salles
        ordinateur_dao.py # Opérations CRUD sur les ordinateurs + interventions
    create_tables.py      # Script de création des tables
    menu.py                # Interface en ligne de commande
    main.py                 # Point d'entrée du programme
    requirements.txt
    README.md
```

## Installation et lancement

Aucune dépendance externe n'est nécessaire.

Au premier lancement, les tables sont créées automatiquement si elles
n'existent pas encore.

## Fonctionnalités

### Salles
- Ajouter, afficher, modifier, supprimer une salle
- Une salle ne peut pas être supprimée si elle contient des ordinateurs

### Ordinateurs
- Ajouter, afficher, modifier, supprimer un ordinateur
- Afficher les ordinateurs d'une salle spécifique
- Rechercher un ordinateur par son code (bonus)
- Filtrer les ordinateurs par marque (bonus)
- L'état d'un ordinateur doit être : BON, MOYEN, MAUVAIS ou HS

### Interventions
- Signaler une intervention sur un ordinateur
- Consulter l'historique des interventions d'un ordinateur

### Rapports
- Nombre d'ordinateurs par salle
- Ordinateurs en mauvais état (MAUVAIS ou HS)
- Salles regroupées par bâtiment
- Statistiques générales (bonus)

## Choix techniques

- Toutes les requêtes SQL utilisent des requêtes **paramétrées** (`?`) afin
  d'éviter les injections SQL.
- Les erreurs de saisie utilisateur (nombres invalides, etc.) sont gérées
  avec des blocs `try/except`.


## Auteurs
Talla Cisse Barro
Ndeye Anta Toure
Mouhamed Fane

Projet réalisé dans le cadre du cours de M. DIALLO - Licence 2 RI.
