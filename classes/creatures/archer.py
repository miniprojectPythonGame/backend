from hero import Hero


class Archer(Hero):
    def __init__(self, hp, strength, intelligence, dexterity, endurance, luck, persuasion, trade, leadership, gold=0,
                 lvl=1):
        Hero.__init__(self, hp, strength, intelligence, dexterity, endurance, luck, persuasion, trade, leadership, gold,
                      lvl)
