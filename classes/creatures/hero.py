from backend.classes.creatures.fightClasses.supportClasses.lvl import Lvl
from backend.classes.creatures.supportFunctions import choseClass


class Hero:
    def __init__(self, name, className, gold=0):
        self.name = name
        self.gold = gold
        self.lvl = Lvl()
        self.heroClass = choseClass(className)