from mymonsters.monster import Monster

dragon = Monster("Dragon", 150, 50)
golem = Monster("Golem", 300, 30)
dragon.print_status()
golem.print_status()
winner = None
while(True):
    dragon.attack(golem)
    if golem.is_down():
        winner = dragon
        break
    golem.attack(dragon)
    if dragon.is_down():
        winner = golem
        break
print("Winner:", winner.name)