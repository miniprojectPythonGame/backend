from src.game_classes.objects.buildings.shops.shop import Shop


class MercenaryShop(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.refresh()

    def refresh(self):
        pass

    def removeItem(self, itemID):
        pass

    def buyFromShop(self, itemID):
        pass

