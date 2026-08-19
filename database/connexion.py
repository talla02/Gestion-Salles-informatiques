import sqlite3
from database.config import DB_NAME


def get_connexion():
    """
    Ouvre une connexion vers la base de données SQLite et la retourne.
    On active les clés étrangères (désactivées par défaut dans SQLite).
    """
    connexion = sqlite3.connect(DB_NAME)
    connexion.execute("PRAGMA foreign_keys = ON")
    return connexion
