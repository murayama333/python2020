import random


class Monster:
    def __init__(self, name, hp, ap):
        self.__name = name
        self.__hp = hp
        self.__ap = ap

    def attack(self, target):
        damage = self.calc_damage()
        self.print_attack_message(target, damage)

        target.hp = target.hp - damage
        if target.hp < 0:
            target.hp = 0
        target.print_status()

    def print_attack_message(self, target, damage):
        print(f"{self.name} attacks {target.name}! damage: {damage}")

    def calc_damage(self):
        return self.ap

    def print_status(self):
        print(f"{self.name:6} HP: {self.hp}")

    @property
    def is_down(self):
        return self.hp <= 0

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def ap(self):
        return self.__ap


class Dragon(Monster):
    def print_attack_message(self, target, damage):
        print(f"{self.name} FIRE!! {target.name}! damage: {damage}")

    def calc_damage(self):
        return int(self.ap + self.ap * random.random())


class Golem(Monster):
    def print_attack_message(self, target, damage):
        print(f"{self.name} BOOM!! {target.name}! damage: {damage}")

    def calc_damage(self):
        if random.randint(0, 1) == 0:
            return self.ap
        return self.ap * 2
