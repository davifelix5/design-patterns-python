"""
PROTOTYPE
Criar uma instância molde para criar cópias de diversos objetos
"""
from __future__ import annotations
from typing import List


class Representation:

    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({f", ".join(params)})'

    def __repr__(self):
        return self.__str__()


class Person(Representation):

    def __init__(self, name: str, lastname: str, birth: int) -> None:
        self.name = name
        self.lastname = lastname
        self.birth = birth
        self.addresses: List[Address] = []

    def add_address(self, address: Address):
        self.addresses.append(address)

    def clone(self, **kwargs):
        from copy import deepcopy
        copied = deepcopy(self)
        copied.__dict__.update(kwargs)
        return copied


class Address(Representation):
    def __init__(self, street: str, number: str):
        self.street = street
        self.number = number


if __name__ == "__main__":
    davi = Person('Davi', 'Felix', 2003)
    davi_address = Address('Av. 9 de Julho', '2005')
    davi.add_address(davi_address)

    esposa_davi = davi.clone(name='Isabella')
    print(davi)
    print(esposa_davi)
