from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics


class Npc:
    def __init__(self, name, taughtStatistics: Statistics, startGoldCost=25, costModifier=5):
        self.name = name
        self.taughtStatistics = taughtStatistics
