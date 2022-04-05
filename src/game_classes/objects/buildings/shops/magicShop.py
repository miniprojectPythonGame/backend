from src.game_classes.objects.buildings.shops.shop import Shop


class MagicShop(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.relevant_item_types = (5, 6, 7, 11, 12)
        self.refresh()

    def refresh(self):
        pass

    def removeItem(self, itemID):
        pass

    def buyFromShop(self, itemID):
        pass
