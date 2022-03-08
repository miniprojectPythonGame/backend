from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics


class Mage:
    def __init__(self):
        self.statistics = Statistics(6, 1, 2, 8, 3, 0, 0, 0)

    def __str__(self):
        return 'Mage'
