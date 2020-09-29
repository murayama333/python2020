from mymonsters.monster import Monster, Dragon, Golem, MonsterParty

dragon = Dragon("Dragon", 150, 50)
golem = Golem("Golem", 300, 30)
party = MonsterParty()
party.add(dragon)
party.add(golem)

party.show_monsters()