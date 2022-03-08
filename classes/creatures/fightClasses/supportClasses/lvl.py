from random import randint
from math import floor


class Lvl:
    def __init__(self, lvl=1):
        self.name = lvl
        self.pointsGainedAfterLvl = 4
        self.expToPreviousLvl = 100
        self.expModifier = 1.4
        self.exp = 0
        self.expToNextLvl = 100
        self.freeDevelopmentPoints = lvl * self.pointsGainedAfterLvl
        self.expModifierIncrementer = 0.1


def addExp(self, expOfOther):
    self.exp += floor(expOfOther * randint(1, 11) / 100)

    if self.exp >= self.expToNextLvl:
        self.expToPreviousLvl = self.expToNextLvl
        self.expToNextLvl += floor(self.expToNextLvl * self.expModifier)
        self.expModifier += self.expModifierIncrementer
        self.name += 1
        self.freeDevelopmentPoints += self.pointsGainedAfterLvl


def usePoints(self):
    if self.freeDevelopmentPoints > 0:
        self.freeDevelopmentPoints -= 1

    return self.freeDevelopmentPoints > 0
