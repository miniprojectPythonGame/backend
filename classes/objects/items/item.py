class Item:
    def __init__(self, name, price, description, onlyTreasure=False):
        self.price = price
        self.name = name
        self.description = description
        self.onlyTreasure = onlyTreasure
