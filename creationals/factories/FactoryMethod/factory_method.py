"""
FACOTORY METHOD
    Cria uma base que define uma classe abstrata par a criação de
objetos, passando para as subclasses a responsabilidade de escolher e criar os
objetos, adiando a insranciação de classes
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, owner):
        self.owner = owner

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


class LuxuryMotorcicle(Vehicle):
    def search_client(self):
        print('A sofisticated motorcicle is serching for a client')


class CentralFactory(ABC):
    def __init__(self, car_type: str, *args, **kwargs):
        self.car = self.get_car(car_type, *args, **kwargs)

    @abstractmethod
    def get_car(self, car_type: str, *args, **kwargs) -> Vehicle: pass

    def search_client(self):
        self.car.search_client()


class NorthSubsidiaryFactory(CentralFactory):

    def get_car(self, car_type: str, *args, **kwargs) -> Vehicle:

        if car_type.lower() == 'luxury car':
            return LuxuryCar(*args, **kwargs)
        if car_type.lower() == 'simple':
            return SimpleCar(*args, **kwargs)
        if car_type.lower() == 'motorcicle':
            return Motorcicle(*args, **kwargs)

        raise TypeError('Não existe esse tipo de carro')


class SouthSubsidiaryFactory(CentralFactory):

    def get_car(self, car_type: str, *args, **kwargs) -> Vehicle:

        if car_type.lower() == 'simple':
            return SimpleCar(*args, **kwargs)
        if car_type.lower() == 'motorcicle':
            return Motorcicle(*args, **kwargs)

        raise TypeError('Não existe esse tipo de carro')


if __name__ == "__main__":
    from random import choice

    north_vehicles = [
        'luxury car',
        'simple',
        'motorcicle',
    ]

    south_vehicles = [
        'simple',
        'motorcicle',
    ]

    # Instead of instancing of a class directly, a factory is being used
    # The client doesn't have to specify the class of the Vehicle needed
    # The real classes are ocult, it's all made a method of another class

    print('Northside cars')
    for c in range(5):
        north_car = NorthSubsidiaryFactory(
            choice(north_vehicles), owner='Davi')
        north_car.search_client()
        print(f'This car belongs to {north_car.car.owner}')
        print()

    print()

    print('Southside cars')
    for c in range(5):
        south_car = SouthSubsidiaryFactory(choice(south_vehicles), 'Carlos')
        south_car.search_client()
        print(f'This car belongs to {south_car.car.owner}')
        print()
