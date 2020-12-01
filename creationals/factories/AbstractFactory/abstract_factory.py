"""
ABSTRACT FACTORY
As factories não retornar diretamente as intâncias, mas têm métodos que
retonarm as intâncias de acordo com necessidades específicas, deixando para
outra classe a responsabilidade de retorná-los
"""
from abc import ABC, abstractmethod


# Vehicle blocks
class LuxuryVehicle(ABC):
    @abstractmethod
    def search_client(self) -> None: pass


class SimpleVehicle(ABC):
    @abstractmethod
    def search_client(self) -> None: pass


# Concrete Vehicles from the Northside
class NorthLuxuryCar(LuxuryVehicle):
    def search_client(self):
        print('A luxury from the northside car is serching for a client')


class NorthSimpleCar(SimpleVehicle):
    def search_client(self):
        print('A simple from the northside car is searching for a client')


class NorthMotorcicle(SimpleVehicle):
    def search_client(self):
        print('A motorcicle from the northside is serching for a client')


class NorthLuxuryMotorcicle(LuxuryVehicle):
    def search_client(self):
        print('A luxury motorcicle from the northside is serching a client')


# Concrete Vehicles from the Southside
class SouthLuxuryCar(LuxuryVehicle):
    def search_client(self):
        print('A luxury from the Southside car is serching for a client')


class SouthSimpleCar(SimpleVehicle):
    def search_client(self):
        print('A simple from the Southside car is searching for a client')


class SouthMotorcicle(SimpleVehicle):
    def search_client(self):
        print('A motorcicle from the Southside is serching for a client')


class SouthLuxuryMotorcicle(LuxuryVehicle):
    def search_client(self):
        print('A luxury motorcicle from the Southside is serching a client')


# Absract factory
class CentralFactory(ABC):

    @staticmethod
    @abstractmethod
    def get_luxury_car() -> LuxuryVehicle: pass

    @staticmethod
    @abstractmethod
    def get_simple_car() -> SimpleVehicle: pass

    @staticmethod
    @abstractmethod
    def get_motorcicle() -> SimpleVehicle: pass

    @staticmethod
    @abstractmethod
    def get_luxury_motorcicle() -> LuxuryVehicle: pass


# Concrete factories
class NorthSubsidiaryFactory(CentralFactory):

    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return NorthLuxuryCar()

    @staticmethod
    def get_simple_car() -> SimpleVehicle:
        return NorthSimpleCar()

    @staticmethod
    def get_motorcicle() -> SimpleVehicle:
        return NorthMotorcicle()

    @staticmethod
    def get_luxury_motorcicle() -> LuxuryVehicle:
        return NorthLuxuryMotorcicle()


class SouthSubsidiaryFactory(CentralFactory):

    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return SouthLuxuryCar()

    @staticmethod
    def get_simple_car() -> SimpleVehicle:
        return SouthSimpleCar()

    @staticmethod
    def get_motorcicle() -> SimpleVehicle:
        return SouthMotorcicle()

    @staticmethod
    def get_luxury_motorcicle() -> LuxuryVehicle:
        return SouthLuxuryMotorcicle()


# Client code
class MainFactory:

    def __init__(self, zone: CentralFactory):
        self.zone = zone

    def search_clients(self):
        """
            O código cliente é escrito do mesmo jeito para ambas as fábricas,
        pois ele está lidando com a interface abstrata CentraFactory.
            No entanto, ele ainda retorna objetos específicos de acordo com a
        instância passada
        """
        simple_car = self.zone.get_simple_car()
        simple_car.search_client()

        luxury_car = self.zone.get_luxury_car()
        luxury_car.search_client()

        simple_motorcicle = self.zone.get_motorcicle()
        simple_motorcicle.search_client()

        luxury_motorcicle = self.zone.get_luxury_motorcicle()
        luxury_motorcicle.search_client()


if __name__ == "__main__":
    north_client = MainFactory(NorthSubsidiaryFactory())
    north_client.search_clients()
    print()
    south_client = MainFactory(SouthSubsidiaryFactory())
    south_client.search_clients()
