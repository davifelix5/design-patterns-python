"""
Strategy
Encapsula diversos métodos diferentes que podem ser implementados e usados
de acordo com a necessidade (open/closed principle)
Exemplo: formas de dar desconto de um pedido
"""
from abc import ABC, abstractmethod
from typing import List


class Representation:

    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({f", ".join(params)})'

    def __repr__(self):
        return self.__str__()


class Product(Representation):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price


# Strategies
class DiscountStrategy(ABC):

    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercentOff(DiscountStrategy):

    def calculate(self, value: float) -> float:
        return value * 0.8


class FiftyPercentOff(DiscountStrategy):

    def calculate(self, value: float) -> float:
        return value * 0.5


class NoDiscount(DiscountStrategy):

    def calculate(self, value: float) -> float:
        return value


class CustumedDiscount(DiscountStrategy):

    def __init__(self, discount: float):
        self._discount = discount

    def calculate(self, value: float) -> float:
        return value * (1 - self._discount)


# Context
class Order(Representation):

    def __init__(self, products: List[Product], discount: DiscountStrategy):
        self._total_value = sum([product.price for product in products])
        self._discount = discount

    @property
    def total(self):
        return self._total_value

    @property
    def subtotal(self):
        return self._discount.calculate(self._total_value)


if __name__ == "__main__":
    products = [
        Product('Nonebook Acer Linux', 500.0),
        Product('Keyboard Razer', 250.0),
        Product('Headphone Razer', 250.0),
    ]

    order1 = Order(products, FiftyPercentOff())
    order2 = Order(products, TwentyPercentOff())
    order3 = Order(products, NoDiscount())
    order4 = Order(products, CustumedDiscount(0.05))

    print('Total 1', end=': ')
    print(order1.total)
    print('Total 2', end=': ')
    print(order2.total)
    print('Total 3', end=': ')
    print(order3.total)
    print('Total 4', end=': ')
    print(order4.total)

    print('Subtotal 1', end=': ')
    print(order1.subtotal)
    print('Subtotal 2', end=': ')
    print(order2.subtotal)
    print('Subtotal 3', end=': ')
    print(order3.subtotal)
    print('Subtotal 4', end=': ')
    print(order4.subtotal)
