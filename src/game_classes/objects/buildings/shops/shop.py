from abc import ABC, abstractmethod

from src.game_classes.objects.items.item import ItemBuilder
from src.web.WebService import connect_to_db, disconnect_from_db


class Shop(ABC):
    def __init__(self, hero_id):
        self.itemList = []
        self.hero_id = hero_id
        self.relevant_item_types = ()

    @abstractmethod
    def removeItem(self, itemID):
        pass  # TODO remove item from the shop adding new random one

    @abstractmethod
    def buyFromShop(self, itemID):
        pass  # TODO take money from hero and give him item, removing item from the shop

    def refresh(self):
        self.itemList = []
        try:
            conn, cursor = connect_to_db()
            select = "SELECT item_id from items where item_type_id in " + str(self.relevant_item_types) + ";"
            cursor.execute(select)
            item_ids = cursor.fetchall()
            for i in item_ids:
                item_id = i[0]
                cursor.execute(
                    "SELECT I.name,I.price,I.description,I.only_treasure,I.item_type_id,I.min_lvl,I.for_class,s.strength,"
                    "s.intelligence,s.dexterity,s.constitution,s.luck,s.persuasion,s.trade,s.leadership,s.protection,s.initiative"
                    " FROM items I JOIN statistics s on s.statistics_id = I.statistics_id WHERE I.item_id = %s;",
                    (item_id,))
                self.itemList.append(ItemBuilder.build_item(item_id,cursor.fetchall()[0]))
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

    def print(self):
        print(type(self).__name__)
        for i in self.itemList:
            print(i)
