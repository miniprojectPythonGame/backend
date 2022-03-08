from backend.classes.creatures.fightClasses.supportClasses.statistics import Statistics
from backend.classes.objects.items.eq.eqItem import EqItem


class Headgear(EqItem):
    def __init__(self, statistics: Statistics = None, name=None, price=None, description=None):
        EqItem.__init__(self, statistics, name, price, description)


