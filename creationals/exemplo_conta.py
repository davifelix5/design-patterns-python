"""
Nesse caso, a factory está sendo instanciada pelo código cliente
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, saldo_inicial: float, proprietario: str):
        self._saldo = saldo_inicial
        self._dono = proprietario

    @property
    def estrato(self):
        import locale

        locale.setlocale(locale.LC_MONETARY, '')
        return locale.currency(self._saldo)

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, value):
        self._saldo += self.value

    @abstractmethod
    def sacar(self, value) -> bool: pass


class Corrente(Conta):
    def __init__(self, saldo_inicial: float, proprietario: str, limite: float):
        super().__init__(saldo_inicial, proprietario)
        self._limite = limite

    def sacar(self, value):
        if self.saldo >= value - self._limite:
            self._saldo -= value
            return True
        return False


class Poupanca(Conta):
    def __init__(self, saldo_inicial: float, proprietario: str, limite: float):
        super().__init__(saldo_inicial, proprietario)

    def sacar(self, value):
        if self.saldo >= value:
            self.saldo -= value
            return True
        return False
