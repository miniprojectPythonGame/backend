class Shop:
    def __init__(self, description,slotAmount):
        self.description = description
        self.slotAmount = slotAmount

    def changeItem(self, itemID):
        pass  # TODO gets random item from the DB and swapps for the item with the itemID == parameter itemID

    def changeAllItemsForTheHero(self, heroID):
        pass  # TODO swapp all items for random ones from the DB for the Hero, charge him money for it

    def removeItem(self, itemID):
        pass  # TODO remove item from the shop adding new random one

    def buyFromShop(self, heroID, itemID):
        pass  # TODO take money from hero and give him item, removing item from the shop
