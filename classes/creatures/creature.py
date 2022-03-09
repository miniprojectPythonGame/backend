from random import randint

from backend.classes.creatures.fightClasses.supportClasses.lvl import Lvl
from backend.classes.creatures.supportFunctions import choseClass


class Creature:
    def __init__(self, name, className, weapon, lvl=1):
        self.name = name
        self.heroClass = choseClass(className)
        self.lvl = Lvl(lvl)
        self.weapon = weapon

    def strongAgainstOtherClass(self, other):
        match type(other).__name__:
            case 'Warrior':
                return self.heroClass.statistics.strength * 2

            case 'Mage':
                return self.heroClass.statistics.intelligence * 2

            case 'Archer':
                return self.heroClass.statistics.dexterity * 2

    def attack(self, other):
        if type(other.heroClass).__name__ == 'Warrior' and other.shield.name is not None:
            if randint(0, 100) < other.shield.blockChance:
                return 'Blocked'
        dmg = self.heroClass.baseDmg - other.strongAgainstOtherClass(self.heroClass)
        if self.weapon.name is not None:
            return dmg * randint(self.weapon.minDmg, self.weapon.maxDmg)
