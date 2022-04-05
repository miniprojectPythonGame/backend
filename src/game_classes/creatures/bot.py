from src.game_classes.creatures.creature import Creature


class Bot(Creature):
    def __init__(self, name, className, lvl=1):
        Creature.__init__(self, name, className, lvl)
        self.heroClass.statistics.setFightStatistics(self.freeDevelopmentPoints)
