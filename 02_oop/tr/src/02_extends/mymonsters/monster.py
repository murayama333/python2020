import random

class Monster:
    def __init__(self, name, hp, ap):
        self.name = name
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

    def is_down(self):
        return self.hp <= 0

class Dragon(Monster):
    def __init__(self, name, hp, ap, mp):
        super().__init__(name, hp, ap)
        self.mp = mp

    def print_attack_message(self, target, damage):
        if self.mp > 0:
            print(f"{self.name} FIRE!! {target.name}! damage: {damage}")
            self.mp = self.mp - 1
        else:
            super().print_attack_message(target, damage)
    
    def calc_damage(self):
        if self.mp > 0:
            return int(self.ap + self.ap * random.random())
        return super().calc_damage()


class Golem(Monster):
    def print_attack_message(self, target, damage):
        print(f"{self.name} BOOM!! {target.name}! damage: {damage}")
    
    def calc_damage(self):
        if random.randint(0, 1) == 0:
            return self.ap
        return self.ap * 2
