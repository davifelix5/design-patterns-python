"""
    Tem a intenção de fornecer um objeto substituto que atua como o objeto que
o cliente deseja utilizar
    Receberá as solicitações e terá como filtrar as solicitações que serão
passadas para o objeto real
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class iUser(ABC):

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class User(iUser):
    """
    Real subject
    """

    def __init__(self, firstname: str, lastname: str):
        print('Fazendo requisicao...')
        sleep(1)  # Simulando requisicao na base dados
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        print('Fazendo requisicao...')
        sleep(1)  # Simulando requisicao
        return [
            {'rua': 'Av. 9 de Julho', 'numero': 2005}
        ]

    def get_all_user_data(self) -> Dict:
        print('Fazendo requisicao...')
        sleep(2)  # Simulando requisicao
        return {'cpf': '125.134.532-23', 'rg': 'AB111222333'}


class UserProxy(iUser):
    """
    Proxy Object
    """

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: User  # Lazy instanciantion
        self._cached_addresses: List[Dict]  # Lazy avaluation
        self._cached_user_data: Dict  # Lazy avaluation

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = User(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        if not hasattr(self, '_cached_user_data'):
            self._cached_user_data = self._real_user.get_all_user_data()
        return self._cached_user_data


if __name__ == "__main__":
    davi = UserProxy('Davi', 'Felix')

    # Primeira requisição
    print(davi.firstname)
    print(davi.lastname)
    print(davi.get_all_user_data())
    print(davi.get_addresses())
    print()
    sleep(1)
    print('=='*25)
    for c in range(10):
        print(davi.get_addresses())
        print(davi.get_all_user_data())
        print()
