import creature


class Hero(creature):
    def __init__(self, hp, strength, intelligence, dexterity, endurance, luck, ability_points=0, gold=0):
        super().__init__(hp, strength, intelligence, dexterity, endurance, luck, ability_points, gold)
