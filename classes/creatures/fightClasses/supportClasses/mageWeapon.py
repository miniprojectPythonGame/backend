from backend.classes.creatures.fightClasses.supportClasses.weapon import Weapon


class MageWeapon(Weapon):
    def __init__(self, minDmg, maxDmg, name, price, description):
        Weapon.__init__(self, minDmg, maxDmg, name, price, description)