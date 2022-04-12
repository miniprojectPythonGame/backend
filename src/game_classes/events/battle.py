from math import floor
from random import randint

from src.game_classes.creatures.creature import Creature
from src.game_classes.creatures.hero import Hero


class Battle(object):
    @classmethod
    def hero_vs_hero(cls, hero_1: Hero, hero_2: Hero):
        chances = hero_1.heroClass.statistics.initiative + hero_2.heroClass.statistics.initiative
        finished = False
        winner = None
        loser = None

        if randint(1, chances) <= hero_1.heroClass.statistics.initiative:
            hero_1_attacks = True
        else:
            hero_1_attacks = False

        while not finished:
            if hero_1_attacks:
                Battle.__hero_attacks(hero_1, hero_2)
                if hero_2.heroClass.statistics.hp <= 0:
                    finished = True
                    winner = hero_1
                    loser = hero_2

            else:
                Battle.__hero_attacks(hero_2, hero_1)
                if hero_1.heroClass.statistics.hp <= 0:
                    finished = True
                    winner = hero_2
                    loser = hero_1
            hero_1_attacks = not hero_1_attacks

        Battle.__transfer_gold_and_exp_between_heroes(winner, loser)

    @classmethod
    def __hero_attacks(cls, creature_1: Hero, creature_2: Creature):
        dmg = randint(1, creature_1.heroClass.baseDmg)
        equipped_weapon = creature_1.eq.itemSlots[9]
        if equipped_weapon is not None:
            dmg *= randint(equipped_weapon.min_dmg, equipped_weapon.max_dmg)
        dmg *= creature_1.strongAgainstOtherClass(creature_2.heroClass)
        dmg = floor(
            dmg / randint(1, creature_2.heroClass.statistics.protection * (1 + creature_2.heroClass.statistics.luck)))
        creature_2.heroClass.statistics.hp -= max(0, dmg)

    @classmethod
    def get_gold_at_stake(cls, hero: Hero, other_creature):
        if type(other_creature).__name__ == "Hero":
            return floor((randint(1, 20) / 100) * other_creature.eq.gold * (other_creature.lvl / hero.lvl))
        if type(other_creature).__name__ == "Bot":
            return other_creature.gold

    @classmethod
    def get_exp_at_stake(cls, hero: Hero, other_creature):
        if type(other_creature).__name__ == "Hero":
            return floor((other_creature.lvl / hero.lvl) * hero.exp * (randint(1, 1000) / 1000))
        if type(other_creature).__name__ == "Bot":
            return other_creature.gained_exp

    @classmethod
    def __transfer_gold_and_exp_between_heroes(cls, winner: Hero, loser: Hero):
        gold_at_stake = Battle.get_gold_at_stake(winner, loser)
        exp_at_stake = Battle.get_exp_at_stake(winner, loser)
        winner.eq.gold += gold_at_stake
        # TODO add gold in db to winner
        winner.addExp(exp_at_stake)
        loser.eq.gold -= gold_at_stake
        # TODO take gold in db from loser
