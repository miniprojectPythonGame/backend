from random import randint


class Statistics:
    def __init__(self, strength, intelligence, dexterity, constitution, luck, persuasion, trade, leadership):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.constitution = constitution
        self.luck = luck

        self.hp = constitution * 100
        self.maxHp = constitution * 100

        self.persuasion = persuasion
        self.trade = trade
        self.leadership = leadership

    def setFightStatistics(self, freeDevelopmentPoints):
        for i in range(0, freeDevelopmentPoints):
            match randint(0, 4):
                case 0:
                    self.strength += 1
                case 1:
                    self.intelligence += 1
                case 2:
                    self.dexterity += 1
                case 3:
                    self.constitution += 1
                case 4:
                    self.luck += 1

        self.hp = self.constitution * 100
        self.maxHp = self.constitution * 100

    def __str__(self):
        return 'strength: ' + str(self.strength) + '\n' + 'intelligence: ' + str(self.intelligence) + \
               '\n' + 'dexterity: ' + str(self.dexterity) + '\n' + 'constitution: ' + str(self.constitution) + \
               '\n' + 'luck: ' + str(self.luck) + '\n' + 'hp: ' + str(self.hp) + \
               '\n' + 'maxHp: ' + str(self.maxHp) + '\n' + 'persuasion: ' + str(self.persuasion) + \
               '\n' + 'trade: ' + str(self.trade) + '\n' + 'leadership: ' + str(self.leadership)
