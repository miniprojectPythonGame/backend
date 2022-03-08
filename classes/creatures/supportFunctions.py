from backend.classes.creatures.fightClasses.archer import Archer
from backend.classes.creatures.fightClasses.warrior import Warrior
from backend.classes.creatures.fightClasses.mage import Mage


def choseClass(className):
    match className:
        case 'Archer':
            return Archer()
        case 'Warrior':
            return Warrior()
        case 'Mage':
            return Mage()
