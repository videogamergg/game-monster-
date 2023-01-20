#jeux monstre
from random import *

class entity:
    def __init__(self, health, damage, velocity, max_health, type, hand):
        self.health = health
        self.damage = damage
        self.velocity = velocity
        self.health = health
        self.type = type
        self.maxhealth = max_health
        self.hand = hand
class waipont:
    def __init__(self, name, damage, munition, range):
        self.name = name
        self.attack = damage
        self.munition = munition
        self.range = range

    def get_damage(self):
        return self.attack

    def get_range(self):
        return self.range

    def get_munition(self):
        return self.munition

#
monster1 = entity(1000, 10, 3, 1000, "tank", "none")
monster2 = entity(250, 20, 10, 250, "speed", "none")
monster3 = entity(750, 15, 7, 750, "brain", "none")
#
waipont1 = waipont("first", 10, 10, 3)
#

def personalisation():
    ch_type = str(input("quel type voullez vous etre(tank, dps, healer)"))
    if ch_type == "tank":
        player = entity(500, 20, 5, 500, "tank", "none" )
    if ch_type == "dps":
        player = entity(200, 60, 20, 200,"dps", "none")
    if ch_type == "healer":
        player = entity(350, 10, 30, 350, "healer", "none")
    print("vous avez choisi le type:", player.type)

    ch_waipont = str(input("quel arme voullez vous choisire(first, )"))
    if ch_waipont == "first":
        player.hand = waipont1.attack

monster_fight = "aucun"

def monster_ch():
    monster = [monster3.type, monster1.type, monster2.type]
    print(monster)
    global monster_fight
    fight = str(input("quelmonstre choisisser vous d'affronter"))
    if fight == monster1.type:
        monster_fight = monster1.type
    if fight == monster2.type:
        monster_figth = monster2.type
    if fight == monster3.type:
        monster_figth = monster3.type

#
game = 1
#

while game == 1:
    monster_ch()
    print(monster_fight)

