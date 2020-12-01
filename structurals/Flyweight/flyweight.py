from __future__ import annotations
from typing import List, Dict


class Client:

    def __init__(self, name: str) -> None:
        self.name = name
        # Intrinsic address data
        self._addresses: List[Address] = []
        # Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """
    Flyweigth Object
    """

    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street,
            address_number,
            address_details,
            self._neighborhood,
            self._zip_code
        )


class AddressFactory:
    _addresses: Dict = {}

    @staticmethod
    def get_key(**kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self.get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando um objeto ja criado')
        except KeyError:
            print('Creating a new object')
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    address = address_factory.get_address(
        street='Rua Rocha',
        neighborhood='Bela Vista',
        zip_code='01313-000'
    )
    address2 = address_factory.get_address(
        street='Rua Rocha',
        neighborhood='Bela Vista',
        zip_code='01313-000'
    )

    davi = Client('Davi')
    davi.add_address(address)
    davi.address_number = '2005'
    davi.address_details = 'ap. 401'
    davi.list_addresses()

    carla = Client('Carla')
    carla.add_address(address)
    carla.address_number = '250A'
    carla.address_details = 'ap. 805'
    carla.list_addresses()

    print(address == address2)
