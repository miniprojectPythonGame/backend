from enum import Enum

from src.game_classes.creatures.statistics import Statistics


class Item:
    def __init__(self, name, price, description, statistics, for_class, item_id):
        self.price = price
        self.name = name
        self.description = description
        self.statistics = statistics
        self.for_class = for_class
        self.item_id = item_id

    def __str__(self):
        return '----------------------\nName: ' + self.name + '\nprice: ' + \
               str(self.price) + '\ndescription: ' + self.description + '\n----------------------'


class ItemType(Enum):
    Belt = 0
    Boots = 1
    Breastplate = 2
    Gloves = 3
    Headgear = 4
    LuckyItem = 5
    Necklace = 6
    Ring = 7
    Steed = 8
    PrimaryWeapon = 9
    SecondaryWeapon = 10
    PotionPeriod = 11
    PotionPermanent = 12


class Belt(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 0


class Boots(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 1


class Breastplate(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 2


class Gloves(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 3


class Headgear(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 4


class LuckyItem(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 5


class Necklace(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 6


class Ring(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 7


class Steed(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, additionalStorage=0):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)
        self.additionalStorage = additionalStorage  # in slots

    @classmethod
    def get_code(cls):
        return 8


class PrimaryWeapon(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 9


class SecondaryWeapon(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    @classmethod
    def get_code(cls):
        return 10


class PotionPeriod(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, periodInDays=7):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)
        self.periodInDays = periodInDays

    def use(self):
        pass

    @classmethod
    def get_code(cls):
        return 11


class PotionPermanent(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id):
        Item.__init__(self, name, price, description, statistics, for_class, item_id)

    def use(self):
        pass

    @classmethod
    def get_code(cls):
        return 12


class ItemBuilder(object):
    @classmethod
    def build_item(cls, item_id, item_info):
        newStats = Statistics(item_info[7],
                              item_info[8],
                              item_info[9],
                              item_info[10],
                              item_info[11],
                              item_info[12],
                              item_info[13],
                              item_info[14],
                              item_info[15],
                              item_info[16],
                              )

        if item_info[4] == ItemType.Belt.value:
            newItem = Belt(newStats,
                           item_info[0],
                           item_info[1],
                           item_info[2], item_info[6], item_id)

        elif item_info[4] == ItemType.Boots.value:
            newItem = Boots(newStats,
                            item_info[0],
                            item_info[1],
                            item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.Breastplate.value:
            newItem = Breastplate(newStats,
                                  item_info[0],
                                  item_info[1],
                                  item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.Gloves.value:
            newItem = Gloves(newStats,
                             item_info[0],
                             item_info[1],
                             item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.Headgear.value:
            newItem = Headgear(newStats,
                               item_info[0],
                               item_info[1],
                               item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.LuckyItem.value:
            newItem = LuckyItem(newStats,
                                item_info[0],
                                item_info[1],
                                item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.Necklace.value:
            newItem = Necklace(newStats,
                               item_info[0],
                               item_info[1],
                               item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.Ring.value:
            newItem = Ring(newStats,
                           item_info[0],
                           item_info[1],
                           item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.Steed.value:
            newItem = Steed(newStats,
                            item_info[0],
                            item_info[1],
                            item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.PrimaryWeapon.value:
            newItem = PrimaryWeapon(newStats,
                                    item_info[0],
                                    item_info[1],
                                    item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.SecondaryWeapon.value:
            newItem = SecondaryWeapon(newStats,
                                      item_info[0],
                                      item_info[1],
                                      item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.PotionPeriod.value:
            newItem = PotionPeriod(newStats,
                                   item_info[0],
                                   item_info[1],
                                   item_info[2], item_info[6], item_id)
        elif item_info[4] == ItemType.PotionPermanent.value:
            newItem = PotionPermanent(newStats,
                                      item_info[0],
                                      item_info[1],
                                      item_info[2], item_info[6], item_id)
        else:
            newItem = -1

        return newItem