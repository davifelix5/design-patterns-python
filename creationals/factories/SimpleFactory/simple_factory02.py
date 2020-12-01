"""
Nesse caso, o client está instancionado factory class
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def search_client(self) -> None: pass


class LuxuryCar(Vehicle):
    def search_client(self):
        print('A luxury car is serching for a client')


class SimpleCar(Vehicle):
    def search_client(self):
        print('A simple car is searching for a client')


class Motorcicle(Vehicle):
    def search_client(self):
        print('A motorcicle is serching for a client')


class VehicleFactory:
    def __init__(self, car_type: str):
        self._carro = self._get_car(car_type)

    @staticmethod
    def _get_car(car_type: str) -> Vehicle:
        if car_type.lower() == 'simple':
            return SimpleCar()
        if car_type.lower() == 'luxury':
            return LuxuryCar()
        if car_type.lower() == 'motorcicle':
            return Motorcicle()
        raise NameError('This car type does not exist')

    def search_client(self):
        self._carro.search_client()


if __name__ == "__main__":
    from random import choice

    available_cars = ['luxury', 'simple', 'motorcicle']
    # Instead of instancing of a class directly, a factory is being used
    # The client doesn't have to specify the class of the Vehicle needed
    # The real classes are ocult, it's all made a method of another class
    for c in range(10):
        carro = VehicleFactory(choice(available_cars))
        carro.search_client()
