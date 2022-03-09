from backend.classes.creatures.fightClasses.supportClasses.weapon import Weapon


class ArcherWeapon(Weapon):
    def __init__(self, minDmg, maxDmg, name, price, description):
        Weapon.__init__(self, minDmg, maxDmg, name, price, description)
