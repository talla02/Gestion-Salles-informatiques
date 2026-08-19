class Salle:
    """Représente une salle informatique."""

    def __init__(self, id=None, nom="", capacite=0, batiment="", date_creation=None):
        self.id = id
        self.nom = nom
        self.capacite = capacite
        self.batiment = batiment
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.nom} - Bâtiment {self.batiment} - Capacité: {self.capacite} places"
