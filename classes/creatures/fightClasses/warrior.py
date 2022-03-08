from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics


class Warrior:
    def __init__(self):
        self.statistics = Statistics(1, 8, 1, 4, 6, 0, 0, 0)

    def __str__(self):
        return 'Warrior'
