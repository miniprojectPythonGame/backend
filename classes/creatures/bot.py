from backend.classes.creatures.creature import Creature
from backend.classes.creatures.fightClasses.supportClasses.weapon import Weapon


class Bot(Creature):
    def __init__(self, name, className, lvl=1):
        Creature.__init__(self, name, className, Weapon(), lvl)
        self.heroClass.statistics.setFightStatistics(self.lvl.freeDevelopmentPoints)
