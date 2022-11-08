"""
This file contains the class Orc which is a subclass Creature, and the class OrcBoss which is a subclass of Orc.

"""

import creature_class


class Orc(creature_class.Creature):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points):
        creature_class.Creature.__init__(self, 'Orc', False, position, image)
        self.__weapon = weapon
        self.__max_hit_points = max_hit_points
        self.__current_hit_points = current_hit_points

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_weapon(self):
        return self.__weapon

    def set_max_hit_points(self, max_hit_points):
        self.__max_hit_points = max_hit_points

    def get_max_hit_points(self):
        return self.__max_hit_points

    def set_current_hit_points(self, current_hit_points):
        self.__current_hit_points = current_hit_points

    def get_current_hit_points(self):
        return self.__current_hit_points

    def __str__(self):
        return f'This Orc uses a(n) {self.__weapon} and has HP: {self.__current_hit_points}/150.\n' \
               f'This unfriendly Orc is located at {creature_class.Creature.get_position(self)} and uses the image asset: ' \
               f'{creature_class.Creature.get_image(self)}\n'


class OrcBoss(Orc):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points, name, special_move):
        Orc.__init__(self, position, image, weapon, max_hit_points, current_hit_points)
        self.__name = name
        self.__special_move = special_move

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_special_move(self, special_move):
        self.__special_move = special_move

    def get_special_move(self):
        return self.__special_move

    def __str__(self):
        return f'{self.__name} is an Orc Boss with {self.__special_move} as a special move.\n' \
               f'This Orc uses a(n) {Orc.get_weapon(self)} and has HP: {Orc.get_current_hit_points(self)}/350.\n' \
               f'This unfriendly Orc is located at {Orc.get_position(self)} and uses the image asset: {Orc.get_image(self)}'


def main():
    lil_orc = Orc((100, -200, 75), 'smeezo.gif', 'mace', 150, 150)
    big_boss = OrcBoss((125, -150, 100), 'mooki.gif', 'warhammer', 350, 350, 'Mooki', 'ground pound')
    
    print(lil_orc)
    print(big_boss)


if __name__ == '__main__':
    main()
