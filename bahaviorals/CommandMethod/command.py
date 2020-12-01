"""
Exemplo da casa inteligente
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Representarion:

    def __str__(self):
        params = [f'{k}={v}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(params)})'

    def __repr__(self):
        return self.__str__()


# Receiver
class Lamp(Representarion):

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.color: str = 'Default'
        self.lighted: bool = False
        self._brightness: float = 100.0

    def on(self) -> None:
        print(f'The lamp "{self.name}" is now ON')
        self.lighted = True

    def off(self) -> None:
        print(f'The lamp "{self.name}" is now OFF')
        self.lighted = False

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'The color of the light "{self.name}" is now {self.color}')

    def setBrightness(self, percentage: float) -> None:
        self.brightness *= percentage

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        old_brightness = self._brightness
        self._brightness = value
        print(
            f'The brightness of the TV went from {old_brightness} to '
            f'{self.brightness}')


# COMMANDS
class iCommand(ABC, Representarion):

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class TurnLampOn(iCommand):

    def __init__(self, receiver: Lamp) -> None:
        self._lamp: Lamp = receiver

    def execute(self) -> None:
        self._lamp.on()

    def undo(self) -> None:
        if self._lamp.lighted:
            self._lamp.off()
        else:
            print(f'The lamp "{self._lamp.name}" is already OFF')


class ChangeLampColor(iCommand):
    def __init__(self, receiver: Lamp, color: str) -> None:
        self._lamp = receiver
        self.new_color = color
        self.old_color = self._lamp.color

    def execute(self) -> None:
        if self._lamp.lighted:
            self._lamp.change_color(self.new_color)
            return
        print('The lamp should be on')

    def undo(self) -> None:
        if self._lamp.lighted:
            self._lamp.change_color(self.old_color)
            return
        print('The lamp should be on')


class ChangeLampBrightness(iCommand):
    """
    Command used to set a new brightness to the lamp

        It takes a float number between one and 0 and multiplies the brightness
    of the lamp for that number
    """

    def __init__(self, receiver: Lamp, new_brightness: float):
        self._lamp = receiver
        self.new_brightness = new_brightness
        self.old_brightness = self._lamp.brightness

    def execute(self) -> None:
        self._lamp.setBrightness(self.new_brightness)

    def undo(self) -> None:
        self._lamp.brightness = self.old_brightness


# INVOKER
class iInvoker(ABC):
    @abstractmethod
    def add_command(self, identificator: int, command: iCommand) -> None: pass

    @abstractmethod
    def execute_command(self, identificator: int) -> None: pass


class RemoteController(iInvoker):

    def __init__(self):
        self._buttons: Dict[int, iCommand] = {}
        self._pressed_buttons: List[int] = []
        self._actions: List[Tuple[iCommand, str]] = []

    def add_command(self, identificator: int, command: iCommand) -> None:
        self._buttons[identificator] = command

    def execute_command(self, identificator: int) -> None:
        command = self._buttons[identificator]
        self._actions.append((command, 'execute'))
        command.execute()

    def undo_command(self, identificator: int) -> None:
        command = self._buttons[identificator]
        self._actions.append((command, 'undo'))
        command.undo()

    def press_button(self, button_id: int):
        if button_id not in self._pressed_buttons:
            self.execute_command(button_id)
            self._pressed_buttons.append(button_id)
            return
        self.undo_command(button_id)
        self._pressed_buttons.remove(button_id)

    def global_undo(self) -> None:
        last_action, action_type = self._actions.pop()
        last_action.execute() if action_type == 'undo' else last_action.undo()

    def undo_all(self):
        while self._actions:
            self.global_undo()


if __name__ == "__main__":
    # Receivers
    bedroom_light = Lamp('Bedroom Light')
    bathroom_ligth = Lamp('Bathroom light')

    # Invokers
    remote_controller = RemoteController()

    # Adicioando os comandos de mudar de cor
    remote_controller.add_command(1, TurnLampOn(bedroom_light))
    remote_controller.add_command(2, TurnLampOn(bathroom_ligth))

    # Adicionando os camandos de mudar a cor
    remote_controller.add_command(3, ChangeLampColor(bedroom_light, 'Red'))
    remote_controller.add_command(4, ChangeLampColor(bathroom_ligth, 'Blue'))

    # Adicionandos os comandos para mudar o brihlo
    remote_controller.add_command(5, ChangeLampBrightness(bedroom_light, 0.25))

    print('---')
    # Ligando as lâmpadas
    remote_controller.press_button(1)
    remote_controller.press_button(2)
    print('---')
    # Setando as cores e voltando para as cores padrões
    remote_controller.press_button(3)
    remote_controller.press_button(4)
    print('---')
    # Mudando o brilho da lâmpada
    remote_controller.press_button(5)
    # Desligando as lâmpadas
    remote_controller.press_button(1)
    remote_controller.press_button(2)
    print('='*45)
    remote_controller.undo_all()
