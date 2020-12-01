"""
Strategy
Encapsula diversos métodos diferentes que podem ser implementados e usados
de acordo com a necessidade (open/closed principle)
Exemplo: formas de dar desconto de um pedido
"""
from typing import List, Callable


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


# Context
class Order(Representation):

    def __init__(
            self, products: List[Product],
            discount: Callable[[float], float] = lambda x: x) -> None:
        self._total_value = sum([product.price for product in products])
        self._discount = discount

    @property
    def total(self):
        return self._total_value

    @property
    def subtotal(self):
        return self._discount(self._total_value)


if __name__ == "__main__":
    products = [
        Product('Nonebook Acer Linux', 500.0),
        Product('Keyboard Razer', 250.0),
        Product('Headphone Razer', 250.0),
    ]

    order1 = Order(products, lambda x: x * 0.5)
    order2 = Order(products, lambda x: x * 0.8)
    order3 = Order(products)
    order4 = Order(products, lambda x: x * 0.95)

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
