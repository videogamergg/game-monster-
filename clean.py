#jeux monstre
from random import *

class entity:
    def __init__(self, type, health, damage, velocity):
        self.type = type
        self.damage = damage
        self.health = health
        self.velocity = velocity


    def entity_builder(filter, filter_value):
        fo = open("player.stat")

        for a_string in fo:
            if "#" in a_string:
                need_name_now = False
                need_health_now = False
                need_damage_now = False
                need_velocity_now = False
                is_passable = False
                if filter == "NAME" and filter_value != a_string[1:]:
                    is_passable = True
                    pass

                w = entity(a_string[1:], None, None, None, None)
                need_health_now = True

            if need_health_now and "health" in a_string:
                if filter == "health" and filter_value != int(a_string.split("=")[1]):
                    w.health = a_string.split("=")[1]
                    is_passable = True
                    pass
                need_health_now = False
                need_ammo_now = True

            if need_ammo_now and "AMMO" in a_string:
                if filter == "AMMO" and filter_value != int(a_string.split("=")[1]):
                    need_health_now = False
                    is_passable = True
                    pass

                w.ammo = a_string.split("=")[1]
                need_ammo_now = False
                need_range_now = True

            if need_range_now and "RANGE" in a_string:
                if filter == "RANGE" and filter_value != int(a_string.split("=")[1]):
                    need_health_now = False
                    need_ammo_now = False
                    is_passable = True
                    pass

                w.range = a_string.split("=")[1]
                need_range_now = False
                need_rarity_now = True

            if need_rarity_now and "RARITY" in a_string:
                if filter == "RARITY" and filter_value != int(a_string.split("=")[1]):
                    need_range_now = False
                    need_health_now = False
                    need_ammo_now = False
                    is_passable = True
                    pass

class weapon:
    def __init__(self, name, damage, ammo, range, rarity):
        self.name = name
        self.attack = damage
        self.ammo = ammo
        self.range = range
        self.rarity = rarity

    def builder_filter_equal(filter, filter_value):
        fo = open("weapon.stat")

        all_weapons = []

        for a_string in fo:
            if "#" in a_string:
                need_rarity_now = False
                need_range_now = False
                need_damage_now = False
                need_ammo_now = False
                is_passable = False
                if filter =="NAME" and filter_value != a_string[1:]:
                    is_passable = True
                    pass

                w = weapon(a_string[1:],None,None,None,None)
                need_damage_now = True


            if need_damage_now and "DAMAGE" in a_string:
                if filter == "DAMAGE" and filter_value != int(a_string.split("=")[1]):
                    w.damage = a_string.split("=")[1]
                    is_passable = True
                    pass
                need_damage_now = False
                need_ammo_now = True


            if need_ammo_now and "AMMO" in a_string:
                if filter == "AMMO" and filter_value != int(a_string.split("=")[1]):
                    need_damage_now = False
                    is_passable = True
                    pass

                w.ammo = a_string.split("=")[1]
                need_ammo_now = False
                need_range_now = True

            if need_range_now and "RANGE" in a_string:
                if filter == "RANGE" and filter_value != int(a_string.split("=")[1]):
                    need_damage_now = False
                    need_ammo_now = False
                    is_passable = True
                    pass

                w.range = a_string.split("=")[1]
                need_range_now = False
                need_rarity_now = True


            if need_rarity_now and "RARITY" in a_string:
                if filter == "RARITY" and filter_value != int(a_string.split("=")[1]):
                    need_range_now = False
                    need_damage_now = False
                    need_ammo_now = False
                    is_passable = True
                    pass

                w.rarity = a_string.split("=")[1]
                need_rarity_now = False
                if not is_passable:
                    all_weapons.append(w)


        return all_weapons

    def builder_filter_greater(filter, filter_value):
            fo = open("weapon.stat")

            all_weapons = []

            for a_string in fo:
                if "#" in a_string:
                    need_rarity_now = False
                    need_range_now = False
                    need_damage_now = False
                    need_ammo_now = False
                    is_passable = False
                    if filter =="NAME":
                        is_passable = True
                        pass

                    w = weapon(a_string[1:],None,None,None,None)
                    need_damage_now = True


                if need_damage_now and "DAMAGE" in a_string:
                    if filter == "DAMAGE" and not filter_value < int(a_string.split("=")[1]):
                        w.damage = a_string.split("=")[1]
                        is_passable = True
                        pass
                    need_damage_now = False
                    need_ammo_now = True


                if need_ammo_now and "AMMO" in a_string:
                    if filter == "AMMO" and not filter_value < int(a_string.split("=")[1]):
                        need_damage_now = False
                        is_passable = True
                        pass

                    w.ammo = a_string.split("=")[1]
                    need_ammo_now = False
                    need_range_now = True

                if need_range_now and "RANGE" in a_string:
                    if filter == "RANGE" and not filter_value < int(a_string.split("=")[1]):
                        need_damage_now = False
                        need_ammo_now = False
                        is_passable = True
                        pass

                    w.range = a_string.split("=")[1]
                    need_range_now = False
                    need_rarity_now = True


                if need_rarity_now and "RARITY" in a_string:
                    if filter == "RARITY" and not filter_value < int(a_string.split("=")[1]):
                        need_range_now = False
                        need_damage_now = False
                        need_ammo_now = False
                        is_passable = True
                        pass

                    w.rarity = a_string.split("=")[1]
                    need_rarity_now = False
                    if not is_passable:
                        all_weapons.append(w)


            return all_weapons

    def builder_filter_lesser(filter, filter_value):
            fo = open("weapon.stat")

            all_weapons = []

            for a_string in fo:
                if "#" in a_string:
                    need_rarity_now = False
                    need_range_now = False
                    need_damage_now = False
                    need_ammo_now = False
                    is_passable = False
                    if filter =="NAME" and filter_value != a_string[1:]:
                        is_passable = True
                        pass

                    w = weapon(a_string[1:],None,None,None,None)
                    need_damage_now = True


                if need_damage_now and "DAMAGE" in a_string:
                    if filter == "DAMAGE" and not filter_value > int(a_string.split("=")[1]):
                        w.damage = a_string.split("=")[1]
                        is_passable = True
                        pass
                    need_damage_now = False
                    need_ammo_now = True


                if need_ammo_now and "AMMO" in a_string:
                    if filter == "AMMO" and not filter_value > int(a_string.split("=")[1]):
                        need_damage_now = False
                        is_passable = True
                        pass

                    w.ammo = a_string.split("=")[1]
                    need_ammo_now = False
                    need_range_now = True

                if need_range_now and "RANGE" in a_string:
                    if filter == "RANGE" and not filter_value > int(a_string.split("=")[1]):
                        need_damage_now = False
                        need_ammo_now = False
                        is_passable = True
                        pass

                    w.range = a_string.split("=")[1]
                    need_range_now = False
                    need_rarity_now = True


                if need_rarity_now and "RARITY" in a_string:
                    if filter == "RARITY" and not filter_value > int(a_string.split("=")[1]):
                        need_range_now = False
                        need_damage_now = False
                        need_ammo_now = False
                        is_passable = True
                        pass

                    w.rarity = a_string.split("=")[1]
                    need_rarity_now = False
                    if not is_passable:
                        all_weapons.append(w)


            return all_weapons





    def get_starting_weapon():
        results = weapon.builder_filter_equal("RARITY",0)
        return results


#    def __init__(self, health, damage, velocity, max_health, type, hand):
monster1 = entity(1000, 10, 3, 1000)
monster2 = entity(250, 20, 10, 250)
monster3 = entity(750, 15, 7, 750)
#     def __init__(self, name, damage, ammo, range):

#

def personalisation():
    do_while = True
    while do_while:
        ch_type = str(input("quel type voullez vous etre(tank, dps, healer)"))

        if ch_type == "tank" or int(ch_type) == 1:
            player = entity(500, 20, 5, 500, "tank", "none" )
            do_while = False

        if ch_type == "dps" or int(ch_type) == 2:
            player = entity(200, 60, 20, 200,"dps", "none")
            do_while = False

        if ch_type == "healer" or int(ch_type) == 3:
            player = entity(350, 10, 30, 350, "healer", "none")
            do_while = False

    print("vous avez choisi le type:", player.type)


    weapons = weapon.get_starting_weapon()

    for i in weapons:
        print(i.name)
    choose_weapon = str(input("queLle arme voulez vous choisir parmis les suivantes \n"))


    if choose_weapon == "first":
        player.hand = weapon1.attack



monster_fight = "aucun"

def monster_choose():
    monster = [monster1.type, monster2.type, monster3.type ]
    print(monster)

    do_while = True

    while do_while:
        global monster_fight
        fight = str(input("quel monstre choisisser vous d'affronter"))
        if fight == monster1.type:
            monster_fight = monster1.type
            do_while = False

        if fight == monster2.type:
            monster_fight = monster2.type
            do_while = False

        if fight == monster3.type:
            monster_fight = monster3.type
            do_while = False


class fight:
    def __init__(self, distance, monster, player):
        self.distance = distance
        self.monster = monster
        self.player = player
        print("vous vous mettez en position d'attaque, vous vous trouvez ?? "+str(distance)+"m du monstre")

        while self.monster[2] > 0 and self.player.health > 0:
            self.player_turn()
            if self.monster[2] < 0:
                print("le monstre est mort !")
            else:
                self.monster_turn()



#
game = 1
#

while game == 1:
    monster_choose()
    print(monster_fight)

    personalisation()

