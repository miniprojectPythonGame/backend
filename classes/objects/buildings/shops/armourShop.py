from backend.classes.objects.buildings.shops.shop import Shop


class ArmourShop(Shop):
    def __init__(self, description, slotAmount):
        Shop.__init__(self, description, slotAmount)

