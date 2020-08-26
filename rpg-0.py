"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""


class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health <= 0:
            print("You are dead.")
            return False
        else:
            return True

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        self.health -= enemy.power

    def alive(self):
        if self.health <= 0:
            print("Goblin is dead.")
            return False
        else:
            return True

    def print_status(self):
        print("The goblin has %d health and %d power." %
            (self.health, self.power))

# class Character(Hero, Goblin):
#     def __init__(self, health, power):
#       self.health = health
#       self.power = power

#     def alive(self):
#         if self.health <= 0:
#             print("You are dead.")




def main():
    hero = Hero(10, 5)

    goblin = Goblin(6, 2)
   
    while goblin.alive() == True and hero.alive() == True:
        hero.print_status()
        goblin.print_status()
        print("What do you want to do? \n 1. fight goblin \n 2. do nothing \n 3. flee \n >")

        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health > 0:
                goblin.attack(hero)
                print("The goblin does %d damage to you." % goblin.power)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %s" % user_input)

        


main()
