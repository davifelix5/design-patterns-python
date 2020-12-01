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
@dataclass
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

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

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


# Hotdog decorator

# Template decorator
class HotdogDecorator(Hotdog):

    def __init__(self, hotdog: Hotdog):
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.hotdog.ingredients


# Concrete decorator
class BaconDecorator(HotdogDecorator):

    def __init__(self, hotdog: Hotdog):
        super().__init__(hotdog)
        self._ingredient = Bacon()

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(
            sum([
                ingredient.price for ingredient in self._ingredients
            ]), 2
        )

    @property
    def name(self) -> str:
        return f'{self.hotdog.name}+{self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients


if __name__ == "__main__":
    hotdog = SimpleHotdog()
    hotdog_with_bacon = BaconDecorator(hotdog)
    hotdog_with_bacon_plus = BaconDecorator(hotdog_with_bacon)

    # O hotdog continua inalterado, pois o decorator mexeu em um deepcopy do
    # seu estado
    print(hotdog)
    print(hotdog_with_bacon)
    print(hotdog_with_bacon_plus)
