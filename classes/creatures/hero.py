from backend.classes.creatures.fightClasses.supportClasses.lvl import Lvl
from backend.classes.creatures.supportFunctions import choseClass
from backend.classes.objects.items.item import Item


class Hero:
    def __init__(self, name, className, gold=0):
        self.name = name
        self.gold = gold
        self.lvl = Lvl()
        self.heroClass = choseClass(className)
        self.storage = []
        self.Eq