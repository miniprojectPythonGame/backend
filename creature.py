class Creature:
    def __init__(self, hp, strength, intelligence, dexterity, endurance, luck, ability_points=0, gold=0):
        self.hp = hp
        self.max_hp = hp
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.endurance = endurance
        self.luck = luck
        self.ability_points = ability_points
        self.lvl = 1
        self.exp = 0
        self.exp_to_next_lvl = 200
        self.__exp_modifier = 2
        self.gold = gold
