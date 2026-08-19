# Les 4 états autorisés pour un ordinateur
ETATS_VALIDES = ["BON", "MOYEN", "MAUVAIS", "HS"]


class Ordinateur:
    """Représente un ordinateur d'une salle."""

    def __init__(self, id=None, code="", marque="", modele="", etat="BON",
                 salle_id=None, date_creation=None):
        self.id = id
        self.code = code
        self.marque = marque
        self.modele = modele
        self.etat = etat
        self.salle_id = salle_id
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.code} - {self.marque} {self.modele} - État: {self.etat} - Salle ID: {self.salle_id}"
