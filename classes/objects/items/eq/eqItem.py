from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics
from backend.classes.objects.items.item import Item


class EqItem(Item):
    def __init__(self, statistics: Statistics, name, price, description):
        self.statistics = statistics
        Item.__init__(self, name, price, description)
