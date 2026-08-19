class Intervention:
    """Représente une intervention faite sur un ordinateur."""

    def __init__(self, id=None, ordinateur_id=None, description="", date_intervention=None):
        self.id = id
        self.ordinateur_id = ordinateur_id
        self.description = description
        self.date_intervention = date_intervention

    def __str__(self):
        return f"[{self.id}] Ordinateur ID {self.ordinateur_id} - {self.description} ({self.date_intervention})"
