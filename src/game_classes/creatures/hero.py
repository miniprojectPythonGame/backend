from math import floor
from random import randint

from src.game_classes.creatures.creature import Creature
from src.game_classes.objects.buildings.cityGuilds import CityGuilds
from src.game_classes.objects.buildings.guild import Guild
from src.game_classes.objects.buildings.market import Market
from src.game_classes.objects.buildings.shops import ArmourShop, Stable, WeaponShop, MagicShop, MercenaryShop, ShopType

from src.game_classes.objects.items.eq import Eq

from src.web.WebService import *


class Hero(Creature):
    def __init__(self, name, className, gold=0, strength=None, intelligence=None,
                 dexterity=None,
                 constitution=None, luck=None, persuasion=None, trade=None, leadership=None, protection=None,
                 initiative=None, lvl=None, exp=None, expToNextLvl=None, freeDevelopmentPts=None, hero_id=None):

        Creature.__init__(self, name, className, lvl, strength, intelligence, dexterity,
                          constitution, luck, persuasion, trade, leadership, protection,
                          initiative, freeDevelopmentPts)
        self.hero_id = hero_id
        self.eq = Eq(hero_id, className, gold)

        self.lvl = lvl
        self.exp = exp
        self.expToNextLvl = expToNextLvl

        self.messages = None  # TODO to implement for notifications after buying selling or fights

        self.armourShop = ArmourShop(hero_id)
        self.magicShop = MagicShop(hero_id)
        self.weaponShop = WeaponShop(hero_id)
        self.stable = Stable(hero_id)  # TODO to be done in the future
        self.guild = Guild(hero_id)  # TODO to be done in the future
        self.cityGuilds = CityGuilds(hero_id)  # TODO to be done in the future
        self.market = Market(hero_id)  # TODO to be done in the future
        self.mercenaryShop = MercenaryShop(hero_id)  # TODO to be done in the future

    def __str__(self):
        return "| hero_id: " + str(self.hero_id) + "| Hero name: " + self.name + "| exp: " + str(self.exp) + \
               "| exp to next lvl: " + str(self.expToNextLvl) + "| lvl: " + str(self.lvl) + " | class: " + \
               str(self.heroClass) + " |\n-----------------------\n" + \
               str(self.heroClass.statistics) + "\n-----------------------\n"

    def addExp(self, expOfOther):
        exp_to_add = floor(expOfOther * randint(1, 26) / 100)
        self.exp += exp_to_add
        try:
            conn, cursor = connect_to_db()
            cursor.execute("CALL add_exp(%s ,%s )", (self.hero_id, exp_to_add))
            conn.commit()
            disconnect_from_db(conn, cursor)
            if self.exp >= self.expToNextLvl:
                self.__updateAfterLvlUp()
                # TODO add some message for the user
            return True
        except Exception as error:
            print("Email already exists " + str(error))
            return False

    def usePoints(self):
        if self.freeDevelopmentPoints > 0:
            self.freeDevelopmentPoints -= 1

        return self.freeDevelopmentPoints > 0

    def __updateAfterLvlUp(self):
        try:
            conn, cursor = connect_to_db()
            cursor.execute("SELECT exp_next_lvl from heroes where hero_id = %s", (self.hero_id,))
            conn.commit()
            self.expToNextLvl = cursor.fetchall()[0][0]
            disconnect_from_db(conn, cursor)

            self.lvl += 1
            self.freeDevelopmentPoints += 4
            return True
        except Exception as error:
            print("Email already exists: " + str(error))
            return False

    def buy_from_shop(self, item_slot_id: int, shop_type: int):
        if shop_type == ShopType.ArmourShop.value:
            bought_item = self.armourShop.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False

        if shop_type == ShopType.MagicShop.value:
            bought_item = self.magicShop.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False

        if shop_type == ShopType.WeaponShop.value:
            bought_item = self.weaponShop.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False

        if shop_type == ShopType.Stable.value:
            bought_item = self.stable.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False
        if shop_type == ShopType.MercenaryShop.value:
            print("Not implemented!")
            return False
        print("Incorrect shop type")
        return False

    def init_fight_with_other_hero(self, hero_id):
        pass
