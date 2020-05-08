#!/usr/bin/env checkio --domain=py run the-warriors

# 
# END_DESC

class Warrior:
    def __init__(self):
        self.maxHealth = 50
        self.attack = 5
        self.health = self.maxHealth
        self.is_alive = True


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    """

    :type unit_1: object
    """
    while unit_1.is_alive == True and unit_2.is_alive == True:
        unit_2.health -= unit_1.attack
        
        if unit_2.health < 1:
            unit_2.is_alive = False
            return True

        unit_1.health -= unit_2.attack
        if unit_1.health < 1:
            unit_1.is_alive = False
            return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")