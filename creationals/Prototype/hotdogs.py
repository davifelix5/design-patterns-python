"""
Decorator method
1. Permite que adicione novos comportamento a objetos ao colocá-lo em wrappers
2. Alternativa mais flexível do que gerança para extensão de funcionalidades
3. Além de implementar a interface do objeto a ser decorado, ele também
recebe esse objeto por meio de composição, o que permite que as sejam delegadas
funcionalidades de volta para o objeto decorado

O design patter decorador é diferente do decorador do python
"""
from __future__ import annotations
from abc import ABC
from copy import deepcopy
from typing import List
from dataclasses import dataclass


# Ingredients
@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.5


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.5


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MachedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = .99


# Hotdogs
class Hotdog(ABC):
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self.ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def add_ingredient(self, ingredient: Ingredient) -> Hotdog:
        cloned = deepcopy(self)
        cloned.name += f'+{ingredient.__class__.__name__}'
        cloned.ingredients.append(ingredient)
        return cloned

    def remove_ingredient(self, ingredient: Ingredient) -> Hotdog:
        cloned = deepcopy(self)
        if ingredient in cloned._ingredients:
            cloned._ingredients.remove(ingredient)
            cloned.name += f'-{ingredient.__class__.__name__}'
        return cloned

    def __str__(self) -> str:
        return f'{self.name}({self.price}, {self.ingredients})'


class SimpleHotdog(Hotdog):

    def __init__(self):
        self._name = 'SimpleHotdog'
        self._ingredients = [Bread(), Sausage(), PotatoSticks()]


class SpecialHotdog(Hotdog):

    def __init__(self):
        self._name = 'SpecialHotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            PotatoSticks(),
            Bacon(),
            Egg(),
            Cheese(),
            MachedPotatoes(),
        ]


if __name__ == "__main__":
    hotdog = SimpleHotdog()
    hotdog_plus = hotdog.add_ingredient(Bacon())\
        .add_ingredient(Cheese())\
        .add_ingredient(Bacon())\
        .remove_ingredient(Bacon())

    special = SpecialHotdog()
    special_minus = special.remove_ingredient(Egg())

    print(hotdog)
    print(hotdog_plus)

    print(special)
    print(special_minus)
