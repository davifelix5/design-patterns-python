from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class AbstractBox(ABC):

    @abstractmethod
    def show_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    @abstractmethod
    def add(self, child: AbstractBox) -> None: pass

    @abstractmethod
    def remove(self, child: AbstractBox) -> None: pass


class Box(AbstractBox):
    """
    Composite
    """

    def __init__(self, name):
        self._name = name
        self._children: List[AbstractBox] = []

    def show_content(self) -> None:
        print(f'\nProdutos da caixa {self._name}:')
        for child in self._children:
            child.show_content()

    def get_price(self) -> float:
        return sum([child.get_price() for child in self._children])

    def add(self, child: AbstractBox) -> None:
        self._children.append(child)

    def remove(self, child: AbstractBox) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(AbstractBox):
    """
    Leaf
    """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def show_content(self) -> None:
        print(f'The product {self.name} costs R${self.price:.2f}')

    def get_price(self) -> float:
        return self.price

    def add(self, child: AbstractBox) -> None:
        print('You cannot add a child to a leaf')

    def remove(self, child: AbstractBox) -> None:
        print('You cannot remove a child from a leaf')


if __name__ == "__main__":
    # Leaves
    shirt = Product('Adidas White Shirt', 50.00)
    notebook = Product('Notebook Acer Linux', 3150.40)
    smartphone = Product('Samsumg Node 10', 1449.90)
    broom = Product('Broom', 25.5)
    vacuum = Product('Vacuum cleaner', 149.9)
    # Composites
    cart = Box('Shopping Cart')  # Criando uma caixa
    gifts = Box('Products for gift')  # Criando uma caixa
    house = Box('House products')

    cart.add(shirt)
    cart.add(notebook)
    cart.add(smartphone)

    gifts.add(shirt)
    gifts.add(notebook)

    house.add(broom)
    house.add(vacuum)

    cart.add(gifts)  # Adicionando uma caixa dentro de uma caixa
    cart.add(house)

    cart.show_content()
    print('-'*55)
    print(f'The total price of your shopping cart is R${cart.get_price():.2f}')
    print('-'*55)
    print(f'You are spending R${gifts.get_price():.2f} just on gifts')
    print(f'You are spending R${house.get_price():.2f} on house products')
