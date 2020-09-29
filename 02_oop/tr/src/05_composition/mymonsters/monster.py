import random


class Monster:
    def __init__(self, name, hp, ap):
        self._name = name
        self.hp = hp
        self.ap = ap

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
        return self._name

    @staticmethod
    def shuffle(monster1, monster2):
        if random.randint(0, 1) == 1:
            return monster2, monster1
        return monster1, monster2


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


class MonsterParty:
    def __init__(self):
        self.monsters = []
    
    def add(self, monster):
        self.monsters.append(monster)

    def show_monsters(self):
        [monster.print_status() for monster in self.monsters]
