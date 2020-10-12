from mymonsters.monster import Monster, Dragon, Golem

dragon = Dragon("Dragon", 150, 50)
golem = Golem("Golem", 300, 30)
dragon.print_status()
golem.print_status()
winner = None
while(True):
    monster1, monster2 = Monster.shuffle(dragon, golem)
    monster1.attack(monster2)
    if monster2.is_down:
        winner = monster1
        break
    monster2.attack(monster1)
    if monster1.is_down:
        winner = monster2
        break
print("Winner:", winner.name)
