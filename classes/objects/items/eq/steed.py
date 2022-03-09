from backend.classes.objects.items.item import Item


class Steed(Item):
    def __init__(self, name=None, price=None, description=None, speed=0, additionalStorage=0):
        Item.__init__(self, name, price, description)
        self.speed = speed
        self.additionalStorage = additionalStorage  # in slots
