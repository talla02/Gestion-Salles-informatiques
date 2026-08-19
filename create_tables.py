"""
Ce script crée les 3 tables de la base de données :
salle, ordinateur, intervention.

On peut le lancer directement avec : python create_tables.py
"""

from database.connexion import get_connexion


def creer_tables():
    connexion = get_connexion()
    curseur = connexion.cursor()

    # Table salle
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS salle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT UNIQUE NOT NULL,
            capacite INTEGER,
            batiment TEXT,
            date_creation TEXT DEFAULT CURRENT_DATE
        )
    """)

    # Table ordinateur
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS ordinateur (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            marque TEXT NOT NULL,
            modele TEXT,
            etat TEXT DEFAULT 'BON',
            salle_id INTEGER,
            date_creation TEXT DEFAULT CURRENT_DATE,
            FOREIGN KEY (salle_id) REFERENCES salle(id) ON DELETE SET NULL
        )
    """)

    # Table intervention
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS intervention (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ordinateur_id INTEGER,
            description TEXT NOT NULL,
            date_intervention TEXT DEFAULT CURRENT_DATE,
            FOREIGN KEY (ordinateur_id) REFERENCES ordinateur(id) ON DELETE CASCADE
        )
    """)

    connexion.commit()
    connexion.close()
    print("Tables créées avec succès.")


if __name__ == "__main__":
    creer_tables()
