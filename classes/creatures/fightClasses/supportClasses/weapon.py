from backend.classes.objects.items.item import Item


class Weapon(Item):
    def __init__(self, minDmg=None, maxDmg=None, name=None, price=None, description=None):
        Item.__init__(self, name, price, description)
        self.minDmg = minDmg
        self.maxDmg = maxDmg
