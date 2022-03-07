from random import randint
from math import floor


class Lvl:
    def __init__(self, lvl):
        self.name = 1
        self.expToPreviousLvl = 100
        self.expModifier = 1.4
        self.exp = 100
        self.expToNextLvl = 150
        self.freeDevelopmentPoints = 0
        self.pointsGainedAfterLvl = 4
        self.expModifierIncrementer = 0.2

        self.speedUpLevels(lvl)

    def addExp(self, expOfOther):
        self.exp += floor(expOfOther * randint(1, 11) / 100)

        if self.exp >= self.expToNextLvl:
            self.expToPreviousLvl = self.expToNextLvl
            self.expToNextLvl = floor(self.expToNextLvl * self.expModifier)
            self.expModifier += self.expModifierIncrementer
            self.name += 1
            self.freeDevelopmentPoints += self.pointsGainedAfterLvl

    def usePoints(self):
        if self.freeDevelopmentPoints > 0:
            self.freeDevelopmentPoints -= 1

        return self.freeDevelopmentPoints > 0

    def speedUpLevels(self, destinationLvl):
        while self.name is not destinationLvl:
            #         TODO needs implementation - used for leveling up bots and mobs
            self.name += 1
        pass
