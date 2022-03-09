from backend.classes.objects.items.item import Item


class Shield(Item):
    def __init__(self, blockChance=None, name=None, price=None, description=None):
        Item.__init__(self, name, price, description)
        self.blockChance = blockChance  # int from 0 to 100
