from typing import List
from abc import ABC


class Kostroma:
    name = 'Kostroma'

    @staticmethod
    def get_orcs():
        print('Orcs hid in the forest')


class Tokyo:
    name = 'Tokyo'

    @staticmethod
    def get_godzilla():
        print('Godzilla stands near a skyscraper')


class Planet(ABC):
    coordinates: List[float]


class Earth(Planet):
    coordinates = [348.73936, 114.20783]


class Jupiter(Planet):
    coordinates = [0.3033, 1.5040]