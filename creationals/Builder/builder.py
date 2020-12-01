"""
BUILDER
Tem a intenção de fragmentar a criação de um objeto complexo de sua real
implementação, permitindo que sejam criados diversos objetos a partir de um
mesmo molde
É como se fosse um Factory Method mais complexo
"""
from abc import ABC, abstractmethod


class Representarion:

    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(params)})'

    def __repr__(self):
        return self.__str__()


# Product
class User(Representarion):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.birth = None
        self.phonenumbers = []
        self.addresses = []


# Builder Interface
class iUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, firstname: str): pass

    @abstractmethod
    def add_lastname(self, lastname: str): pass

    @abstractmethod
    def add_birth(self, birth: int): pass

    @abstractmethod
    def add_phonenumber(self, phonenumber: str): pass

    @abstractmethod
    def add_address(self, address: str): pass


# Builder Concrete
class UserBuilder(iUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        """
        Define uma instância da classe usuário que poderá ser retornada para
        o cliente e pode ser manipulada para ser criado de maneiras diferentes
        """
        self._result = User()

    def get_result(self) -> User:
        """
        Método que retorna o resultado sem resetá-lo
        """
        return self._result

    def add_firstname(self, firstname: str):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname: str):
        self._result.lastname = lastname
        return self

    def add_birth(self, birth: int):
        self._result.birth = birth
        return self

    def add_phonenumber(self, phonenumber: str):
        self._result.phonenumbers.append(phonenumber)
        return self

    def add_address(self, address: str):
        self._result.addresses.append(address)
        return self

    @property
    def result(self):
        """
        Toda vez que o result for pedido, esse método retornará o usuário que
        foi configurado e depois irá criar outro usuário
        """
        return_data = self.get_result()
        self.reset()
        return return_data


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def user_from_age(self, firstname: str, lastname: str, age: int):
        from datetime import datetime
        current_year = datetime.now().year
        birth = current_year - age

        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_birth(birth)

        return self._builder.result

    def with_address(self, firstname, lastname, address):
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)
        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.user_from_age('Davi', 'Felix', 16)
    user2 = user_director.with_address('Davi', 'Felix', 'Avenida 9 de Julho')
    print(user1)
    print(user2)
