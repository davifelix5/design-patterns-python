"""
Monostate é uma variação do Singleton
Enquanto o Singleton preza por retornar as mesms intâncias, no Monostate,
as instâncias podem ser diferentes, mas elas devem compartilhar estados
"""


class RepresentationMixing:
    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(params)})'

    def __repr__(self):
        return self.__str__()


class A(RepresentationMixing):
    def __init__(self, nome):
        self.x = 10
        self.y = 20
        self.nome = nome


class SimpleMonostate(RepresentationMixing):
    _state: dict = {}

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state
        if nome:
            self.nome = nome
        if sobrenome:
            self.sobrenome = nome


if __name__ == "__main__":
    a = A('Carlos')
    print(a)
    monostate1 = SimpleMonostate()
    monostate2 = SimpleMonostate()
    monostate1.nome = 'Davi'
    monostate2.sobrenome = 'Felix'
    # O sobrenome e o nome foram mandados para classes diferentes, mas as duas
    # possuem os mesmos atributos, pois têm um ESTADO COMPARTILHADO
    print(monostate1, monostate2)
