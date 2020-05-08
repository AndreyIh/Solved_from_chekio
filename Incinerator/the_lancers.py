#!/usr/bin/env checkio --domain=py run the-lancers

# 
# END_DESC

# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

# Taken from mission The Warriors

# Taken from mission The Warriors

class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.vampirism = 0
        self.attack_second = 0

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
        
class Rookie(Warrior):
    
    def __init__(self):
        super().__init__()
        self.attack = 1

class Defender(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 60
        self.defense = 2
        self.attack = 3

    def __str__(self):
        return f'Defender {self.health} hp'

class Vampire(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50

    def __str__(self):
        return f'Vamp {self.health} hp'

class Lancer(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 6
        self.attack_second = 0.5
        

    def __str__(self):
        return f'Lancer {self.health} hp'
        
class Army:

    def __init__(self):
        self.army = []

    def add_units(self, cls, q):
        for i in range(0, q):
            self.army.append(cls())

    @property
    def is_alive(self):
        return False if len(self.army) <= 0 else True

    def __str__(self):
        return f'Knight {self.army}'

class Battle:

    
    def fight(self, army1, army2):
        print(f'{army1.army}')
        print(f'{army2.army}')
        while army1.is_alive and army2.is_alive:
            z1,z2 = 0,0
            if len(army1.army) > 1:
                z1 = army1.army[1]
            if len(army2.army) > 1:
                z2 = army2.army[1]
            res = fight(army1.army[0], army2.army[0], z1, z2)
            if res:
                army2.army.pop(0)
                print('army2', len(army2.army), f'{army2.army}')
            else:
                army1.army.pop(0)
                print('army1', len(army1.army), f'{army1.army}')
            
            
        if army1.is_alive:
            # print (army1)
            return True
        else:
            # print(army2)
            return False
        

def hit_hp(unit_1, unit_2, unit_3 = 0):
    if unit_1.attack > unit_2.defense:
        unit_2.health += - (unit_1.attack - unit_2.defense)
        if unit_2.health > 0:
            unit_1.health += (unit_1.attack - unit_2.defense) * (unit_1.vampirism / 100)
        else:
            unit_1.health += (unit_1.attack - unit_2.defense + unit_2.health) * (unit_1.vampirism / 100)
        if unit_1.attack_second and unit_3:
            unit_3.health +=((unit_1.attack - unit_2.defense)) * unit_1.attack_second
            #temp = ((unit_1.attack - unit_2.defense)) * unit_1.attack_second
            #if temp > unit_3.defense:
                #unit_3.health += - (temp - unit_3.defense)
                #print('second unit', unit_3)
        # print(unit_2, unit_1.attack, unit_2.defense, unit_1)
    else:
        unit_2.health += 0
        #print(unit_2)

def fight(unit_1, unit_2, unit_12 = 0, unit_22 = 0,):
    """
    :type unit_1: object
    """
    while unit_1.is_alive and unit_2.is_alive:
        hit_hp(unit_1, unit_2, unit_12)
        if not unit_2.is_alive:
            print(unit_1)
            return True
        hit_hp(unit_2, unit_1, unit_22)
        if not unit_1.is_alive:
            print(unit_2)
            return False




"""
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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
    print('ПОКА ВСЕ НОРМ!!!')"""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    """chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    
    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)"""

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    #assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")