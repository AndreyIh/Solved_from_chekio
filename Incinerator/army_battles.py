#!/usr/bin/env checkio --domain=py run army-battles

# 
# END_DESC

# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50

    @property
    def is_alive(self):
        return False if self.health <= 0 else True

    def __str__(self):
        return f'Warrior {self.health} hp'

class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7

    def __str__(self):
        return f'Knight {self.health} hp'

class Army:

    def __init__(self):
        self.army = {}

    def add_units(self, cls, q):
        self.army[cls] = q

    @property
    def is_alive(self):
        return False if sum(self.army.values()) <= 0 else True

    def __str__(self):
        return f'Knight {self.army}'

class Battle:

    def creatwar(self, army, k=0):

        for i in army.army.keys():
            if army.army.get(i) > 0:
                unit = i()
                army.army[i] += -1 + k
                return unit

    def fight(self, army1, army2):
        unit1 = self.creatwar(army1, 1)
        unit2 = self.creatwar(army2, 1)

        while army1.is_alive and army2.is_alive:
            if unit1 and unit2:
                res = fight(unit1, unit2)
            if res:
                unit2 = self.creatwar(army2)
            else:
                unit1 = self.creatwar(army1)
        if army1.is_alive:
            print (army1)
            return True
        elif army2.is_alive:
            print(army2)
            return False
        elif fight(unit1, unit2):
            print(army1)
            return True
        else:
            print(army2)
            return False


def fight(unit_1, unit_2):
    """
    :type unit_1: object
    """
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            # print(unit_1)
            return True
        unit_1.health -= unit_2.attack
        if not unit_1.is_alive:
            # print(unit_2)
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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
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

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")