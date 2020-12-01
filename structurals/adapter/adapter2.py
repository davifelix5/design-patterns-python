"""
Contexto:
Fazer um programa que tenha figuras de diversos tipos
Depois fazer um esquema para verificar se essas figuras encaixam em um círculo
de raio x
É preciso adaptar as figuras para pegar seus raios
"""

from abc import ABC, abstractmethod


class RoundPeg(ABC):

    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    @abstractmethod
    def radius(self) -> float: pass


class Cylinder(RoundPeg):

    @property
    def radius(self):
        return self._radius


class SquarePeg(ABC):
    def __init__(self, width: float) -> None:
        self._width = width

    @property
    @abstractmethod
    def width(self) -> float: pass


class Parallelepided(SquarePeg):

    @property
    def width(self) -> float:
        return self._width


class RoundHole():

    def __init__(self, radius: float) -> None:
        self._radius = radius

    def radius(self) -> float:
        return self._radius

    def fits(self, peg: RoundPeg) -> bool:
        """
        Analises if this round hole can fit another round peg
        this will happen if the two object have the same radius or greater
        """
        return self._radius >= peg.radius


class SquarePegAdapter(RoundPeg):

    def __init__(self, square_peg: SquarePeg):
        self.base_peg = square_peg

    @property
    def radius(self) -> float:
        from math import sqrt
        return self.base_peg.width * sqrt(2) / 2


if __name__ == "__main__":
    hole = RoundHole(20)
    cylinder = Cylinder(15)
    parallelepided = Parallelepided(20)
    parallelepided_adapter = SquarePegAdapter(parallelepided)

    print(hole.fits(cylinder))

    # hole.fits(parallelepided) // Erro
    # Dá erro pq o parelelepípedo não tem raio, por isso, é preciso adaptá-lo

    print(hole.fits(parallelepided_adapter))
