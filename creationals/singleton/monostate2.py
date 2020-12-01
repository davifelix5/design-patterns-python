"""
O atributo de classe é declarado como uma cópia dos __dict__ da instância
Esse atributo será compartilhado por todas as classes que herdarem da classe
na qual ele foi definido
Portanto, todas as classes parentes terão o mesmo __dict__
"""


class RepresentationMixing:
    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(params)})'

    def __repr__(self):
        return self.__str__()


class Monostate(RepresentationMixing):

    _state: dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None):
        if nome:
            self.nome = nome
        if sobrenome:
            self.sobrenome = sobrenome


class MonostateChild(Monostate):
    def __init__(self, nome=None, sobrenome=None, emprego=None):
        super().__init__(nome, sobrenome)
        if emprego:
            self.emprego = emprego


if __name__ == "__main__":
    parent_monostate = Monostate('Davi', 'Felix')
    child_monostate = MonostateChild('Clovis', 'Costa', 'UX Designer')

    parent_monostate.nome = 'Joao'
    print(parent_monostate, child_monostate)

    child_monostate.nome = 'Carlos'
    print(parent_monostate, child_monostate)
