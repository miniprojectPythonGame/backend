from backend.classes.creatures.fightClasses.supportClasses.lvl import Lvl
from backend.classes.creatures.supportFunctions import choseClass


class Bot:
    def __init__(self, name, className, lvl=1):
        self.name = name
        self.heroClass = choseClass(className)
        self.lvl = Lvl(lvl)
        self.heroClass.statistics.setFightStatistics(self.lvl.freeDevelopmentPoints)
