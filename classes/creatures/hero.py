from backend.classes.creatures.fightClasses.supportClasses.lvl import Lvl
from backend.classes.creatures.supportFunctions import choseClass
from backend.classes.objects.items.eq.eq import Eq
from backend.classes.objects.items.storage import Storage


class Hero:
    def __init__(self, name, className, gold=0):
        self.name = name
        self.gold = gold
        self.lvl = Lvl()
        self.heroClass = choseClass(className)
        self.Eq = Eq()
        self.storage = Storage()
