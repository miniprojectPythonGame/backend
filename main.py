from backend.classes.creatures.bot import Bot
from backend.classes.creatures.hero import Hero

if __name__ == '__main__':
    hero = Hero('Bob', 'Warrior')
    bot = Bot('Pat', 'Warrior', 50)
    print(hero.heroClass.statistics)
    print('******************************')
    print(bot.heroClass.statistics)
