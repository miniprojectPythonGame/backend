from backend.classes.creatures.creature import Creature
from backend.classes.creatures.fightClasses.supportClasses.weapon import Weapon
from backend.classes.objects.items.eq.eq import Eq
from backend.classes.objects.items.eq.steed import Steed
from backend.classes.objects.items.storage import Storage


class Hero(Creature):
    def __init__(self, name, className, gold=0):
        Creature.__init__(self, name, className, Weapon(), 1)
        self.gold = gold
        self.Eq = Eq()
        self.storage = Storage()
        self.steed = Steed()

    def changeSteed(self, newSteed: Steed):
        if self.steed.name is not None:
            self.storage.freeSpace -= self.steed.additionalStorage
        if newSteed.name is not None:
            self.storage.freeSpace += newSteed.additionalStorage
            self.steed = newSteed
