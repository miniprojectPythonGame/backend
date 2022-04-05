from random import randint

from src.game_classes.creatures.creature import Creature


class Battle:
    def __init__(self, fighterA: Creature, fighterB: Creature):
        self.fighterA = fighterA
        self.fighterB = fighterB

    def whoStarts(self):
        if randint(1, self.fighterA.heroClass.statistics.luck + self.fighterB.heroClass.statistics.luck) <= \
                self.fighterA.heroClass.statistics.luck:
            return self.fighterA

        return self.fighterB
