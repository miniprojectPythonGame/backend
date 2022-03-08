from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics
from backend.classes.objects.items.item import Item


class PotionPeriod(Item):
    def __init__(self, name, price, description, statistics: Statistics, periodInDays):
        Item.__init__(self, name, price, description)
        self.statistics = statistics
        self.periodInDays = periodInDays

    def use(self):
        pass


class PotionPermanent(Item):
    def __init__(self, name, price, description, statistics: Statistics):
        Item.__init__(self, name, price, description)
        self.statistics = statistics

    def use(self):
        pass