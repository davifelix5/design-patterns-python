"""
Nesse caso, o client está usando o próprio objeto, a factory so esta criando
SITUAÇÂO:
Estrutura do Uber
Classes:
    Um cliente precisa de um carro, que pode ser de vários tipos
"""
from abc import ABC, abstractmethod


class Veicle(ABC):
    @abstractmethod
    def search_client(self) -> None: pass


class VeicleFactory:
    """
    This class can manage the instances created in the client code
    """
    @staticmethod
    def get_car(car_type: str) -> Veicle:
        if car_type.lower() == 'simple':
            return SimpleCar()
        if car_type.lower() == 'luxury':
            return LuxuryCar()
        if car_type.lower() == 'motorcicle':
            return Motorcicle()
        raise NameError('This car type does not exist')


class LuxuryCar(Veicle):
    def search_client(self):
        print('A luxury car is serching for a client')


class SimpleCar(Veicle):
    def search_client(self):
        print('A simple car is searching for a client')


class Motorcicle(Veicle):
    def search_client(self):
        print('A motorcicle is serching for a client')


if __name__ == "__main__":
    from random import choice

    available_cars = ['luxury', 'simple', 'motorcicle']
    # Instead of instancing of a class directly, a factory is being used
    # The client doesn't have to specify the class of the veicle needed
    # The real classes are ocult, it's all made a method of another class
    for c in range(10):
        carro = VeicleFactory.get_car(choice(available_cars))
        carro.search_client()
