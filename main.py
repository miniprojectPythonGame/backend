from backend.classes.creatures.bot import Bot
from backend.classes.creatures.hero import Hero
from backend.classes.objects.items.eq.boots import Boots

if __name__ == '__main__':
    # hero = Hero('Bob', 'Warrior')
    # bot = Bot('Pat', 'Warrior', 50)
    # print(hero.heroClass.statistics)
    # print('******************************')
    # print(bot.heroClass.statistics)
    a = Boots()
    print(type(a).__name__)