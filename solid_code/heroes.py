from antagonistfinder import AntagonistFinder
from abc import abstractmethod


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    @abstractmethod
    def attack(self):
        pass


class Kick:
    @staticmethod
    def roundhouse_kick():
        print('Bump')


class LaserEye:
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class Gun:
    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class TaekwondoHero(SuperHero, Kick):
    def attack(self):
        self.roundhouse_kick()


class ShootingHero(SuperHero, Gun):
    def __init__(self, name, can_use_ultimate_attack=True):
        super().__init__(name, can_use_ultimate_attack)

    def attack(self):
        self.fire_a_gun()


class EyeLasersHero(SuperHero, LaserEye):
    def __init__(self, name, can_use_ultimate_attack=True):
        super().__init__(name, can_use_ultimate_attack)

    def attack(self):
        self.incinerate_with_lasers()

    def ultimate(self):
        if self.name == 'Clark Kent':
            self.incinerate_with_lasers()


class Superman(EyeLasersHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return 'Kick'


class TV:
    def __init__(self):
        self.name = 'Fox news'

    @staticmethod
    def create_news(place, name):
        place_name = getattr(place, 'name', 'place')
        print(f'{name} saved the {place_name}!')

    def planets(self, planet):
        planet_coordinates = getattr(planet, 'coordinates', 'place')
        print(f'{self.name} notifies {planet_coordinates}')