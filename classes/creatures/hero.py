from backend.classes.objects.lvl import Lvl


class Hero(Lvl):
    def __init__(self, hp, strength, intelligence, dexterity, endurance, luck, persuasion, trade, leadership, gold=0,
                 lvl=1):
        self.hp = hp
        self.max_hp = hp

        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.endurance = endurance
        self.luck = luck
        self.exp = 0
        self.exp_to_next_lvl = 200
        self.__exp_modifier = 2
        self.gold = gold
        self.persuasion = persuasion
        self.trade = trade
        self.leadership = leadership
        self.lvl = Lvl.__init__(self, lvl)
