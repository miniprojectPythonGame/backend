from backend.classes.objects.buildings.shops.shop import Shop


class WeaponShop(Shop):
    def __init__(self, description, slotAmount):
        Shop.__init__(self, description, slotAmount)

