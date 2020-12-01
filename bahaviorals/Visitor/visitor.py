from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Insurance(ABC):

    @abstractmethod
    def for_residencial_building(self, building: ResidencialBuilding): pass

    @abstractmethod
    def for_bank(self, bank: Bank): pass

    @abstractmethod
    def for_coffe_house(self, coffe_house: CoffeHouse): pass


class InsuranceCompany(Insurance):

    def for_residencial_building(self, building: ResidencialBuilding):
        building.insurances.append(
            'Medical and structural insurance for the residents')

    def for_bank(self, bank: Bank):
        bank.insurances.append('Insurante against robbery')

    def for_coffe_house(self, coffe_house: CoffeHouse):
        coffe_house.insurances.append('Insurance against acidents and floods')


class Stablishment(ABC):

    def __init__(self, name: str):
        self.name = name
        self.insurances: List[str] = []

    @abstractmethod  # Método que aceita visitantes
    def make_insurance(self, visitor: Insurance): pass


class ResidencialBuilding(Stablishment):

    def make_insurance(self, visitor: Insurance):
        print(f'The {self.__class__.__name__} got', end=' ')
        visitor.for_residencial_building(self)
        print(self.insurances)


class Bank(Stablishment):

    def make_insurance(self, visitor: Insurance):
        print(f'The {self.__class__.__name__} got', end=' ')
        visitor.for_bank(self)
        print(self.insurances)


class CoffeHouse(Stablishment):

    def make_insurance(self, visitor: Insurance):
        print(f'The {self.__class__.__name__} got', end=' ')
        visitor.for_coffe_house(self)
        print(self.insurances)


if __name__ == "__main__":
    building = ResidencialBuilding('Plaza')
    bank = Bank('Banco do Brasil')
    coffe_house = CoffeHouse('Central Perk')
    insurance = InsuranceCompany()

    building.make_insurance(insurance)
    print()
    bank.make_insurance(insurance)
    print()
    coffe_house.make_insurance(insurance)
