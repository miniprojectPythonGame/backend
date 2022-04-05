from random import randint

from src.game_classes.creatures.fightClasses import choseClass


class Creature:
    def __init__(self, name, className, lvl, strength=None, intelligence=None, dexterity=None,
                 constitution=None, luck=None, persuasion=None, trade=None, leadership=None, protection=None,
                 initiative=None, freeDevelopmentPts=None):
        self.name = name
        self.heroClass = choseClass(className, strength, intelligence, dexterity,
                                    constitution, luck, persuasion, trade, leadership, protection,
                                    initiative)
        self.lvl = lvl
        self.freeDevelopmentPoints = freeDevelopmentPts
        # self.weapon = weapon  # TODO fix me needs implementation

    def strongAgainstOtherClass(self, other):
        if type(other).__name__ == 'Warrior':
            return self.heroClass.statistics.strength * 2
        if type(other).__name__ == 'Mage':
            return self.heroClass.statistics.intelligence * 2
        if type(other).__name__ == 'Archer':
            return self.heroClass.statistics.dexterity * 2


# def attack(self, other):
#     if type(other.heroClass).__name__ == 'Warrior' and other.shield.name is not None:
#         if randint(0, 100) < other.shield.blockChance:
#             return 'Blocked'
#
#     dmg = self.heroClass.baseDmg - other.strongAgainstOtherClass(self.heroClass)
#     if self.weapon.name is not None:
#         return dmg * randint(self.weapon.minDmg, self.weapon.maxDmg)
