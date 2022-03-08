from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics
from backend.classes.objects.items.eq.belt import Belt
from backend.classes.objects.items.eq.boots import Boots
from backend.classes.objects.items.eq.breastplate import Breastplate
from backend.classes.objects.items.eq.eqItem import EqItem
from backend.classes.objects.items.eq.gloves import Gloves
from backend.classes.objects.items.eq.headgear import Headgear
from backend.classes.objects.items.eq.luckyItem import LuckyItem
from backend.classes.objects.items.eq.necklace import Necklace
from backend.classes.objects.items.eq.ring import Ring


class Eq:
    def __init__(self):
        self.belt = Belt()
        self.boots = Boots()
        self.breastplate = Breastplate()
        self.gloves = Gloves()
        self.headgear = Headgear()
        self.luckyItem = LuckyItem()
        self.necklace = Necklace()
        self.ring = Ring()
        self.gearStatistics = Statistics()

    def changeEqItem(self, oldItem: EqItem, newItem: EqItem):
        if oldItem is not None:
            self.gearStatistics -= oldItem.statistics
        if newItem is not None:
            self.gearStatistics += newItem.statistics
            match type(newItem):
                case type(self.belt):
                    self.belt = newItem

                case type(self.boots):
                    self.boots = newItem

                case type(self.breastplate):
                    self.breastplate = newItem

                case type(self.gloves):
                    self.gloves = newItem

                case type(self.headgear):
                    self.headgear = newItem

                case type(self.luckyItem):
                    self.luckyItem = newItem

                case type(self.necklace):
                    self.necklace = newItem

                case type(self.ring):
                    self.ring = newItem
