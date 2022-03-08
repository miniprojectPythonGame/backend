from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics


class Archer:
    def __init__(self):
        self.statistics = Statistics(1, 2, 7, 6, 4, 0, 0, 0)

    def __str__(self):
        return 'Archer'
