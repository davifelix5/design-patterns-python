"""
    Serve par ligar duas classes diferentes
"""
from abc import ABC, abstractmethod


class iGameControl(ABC):

    @abstractmethod
    def left(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def up(self) -> None: pass


class GameControl(iGameControl):

    def left(self) -> None:
        print('Moving left')

    def right(self) -> None:
        print('Moving right')

    def down(self) -> None:
        print('Moving down')

    def up(self) -> None:
        print('Moving up')


class NewGameControl:

    def move_left(self) -> None:
        print('Moving to the elft direction')

    def move_right(self) -> None:
        print('Moving to the right direction')

    def move_down(self) -> None:
        print('Moving to the down direction')

    def move_up(self) -> None:
        print('Moving to the up direction')


class GameControlAdapter(iGameControl, NewGameControl):
    """
    Adaptador usando herança
    """
    def left(self) -> None:
        self.move_left()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def up(self) -> None:
        self.move_up()


class GameControlAdapter2:
    """
    Adaptador usando composição
    """
    def __init__(self, adaptee: NewGameControl):
        self.adaptee = NewGameControl()

    def left(self) -> None:
        self.adaptee.move_left()

    def right(self) -> None:
        self.adaptee.move_right()

    def down(self) -> None:
        self.adaptee.move_down()

    def up(self) -> None:
        self.adaptee.move_up()


if __name__ == "__main__":
    control = GameControl()
    new_control = GameControlAdapter()
    new_control2 = GameControlAdapter2(new_control)

    control.right()
    control.up()
    control.left()
    control.down()
    print()
    new_control.right()
    new_control.up()
    new_control.left()
    new_control.down()
    print()
    new_control2.right()
    new_control2.up()
    new_control2.left()
    new_control2.down()
