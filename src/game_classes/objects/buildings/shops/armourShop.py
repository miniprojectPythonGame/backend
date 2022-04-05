from src.game_classes.objects.buildings.shops.shop import Shop


class ArmourShop(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.relevant_item_types = (0, 1, 2, 3, 4)
        self.refresh()

    def removeItem(self, itemID):
        pass

    def buyFromShop(self, itemID):
        pass
