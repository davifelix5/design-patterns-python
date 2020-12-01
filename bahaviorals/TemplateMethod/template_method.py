"""
Template method: define um método final que pode ser personalizado pelas
classes filhas
"""
from abc import ABC, abstractmethod


class Pizza(ABC):

    def prepare(self):
        self.add_ingredients()
        self.extra_cheese()
        self.cut()
        self.cook()
        self.serve()

    @abstractmethod
    def add_ingredients(self): pass

    def extra_cheese(self): pass

    @abstractmethod
    def cook(self): pass

    def cut(self):
        print(f'Cutting the pizza {self.__class__.__name__}')

    def serve(self):
        print(f'Serveing the pizza {self.__class__.__name__}')


class CheesePizza(Pizza):
    def add_ingredients(self):
        print('Adding, cheese, tomatto, oregano to cheese pizza')

    def extra_cheese(self):
        print('Adding more cheese no cheese pizza')

    def cook(self):
        print('Cooking the cheese pizza for 45 minutes')


class VeganPizza(Pizza):

    def add_ingredients(self):
        print('Adding vegan cheese, oregano, tomatto')

    def cook(self):
        print('Cooking vegan pizza for 30 minutes')


if __name__ == "__main__":
    cheese = CheesePizza()
    cheese.prepare()
    print()
    vegan = VeganPizza()
    vegan.prepare()
