from __future__ import annotations
from copy import deepcopy
from typing import Dict, List


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        # Setando atributo de uma classe imutável
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name, value) -> None:
        raise AttributeError('This class is immutable')


class ImageEditor:

    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class CareTaker:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:

        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor('foto1.jpg', 200, 100)
    care_taker = CareTaker(img)

    print(img)
    care_taker.backup()

    img.width = 1000
    img.height = 500
    print(img)
    care_taker.backup()

    img.width = 2000
    img.height = 1000
    print(img)

    print()

    care_taker.restore()
    print(img)

    care_taker.restore()
    print(img)
