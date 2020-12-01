from __future__ import annotations
from abc import ABC, abstractmethod


class iRemoteControl(ABC):

    @abstractmethod
    def volume_up(self) -> None: pass

    @abstractmethod
    def volume_down(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass


class RemoteControl(iRemoteControl):

    def __init__(self, device: iDevice):
        self._implementor = device

    def volume_up(self) -> None:
        self._implementor.volume += 10

    def volume_down(self) -> None:
        self._implementor.volume -= 10

    def power(self) -> None:
        self._implementor.power = not self._implementor.power


class RemoteControlWithMute(RemoteControl):

    def mute(self):
        print('Muted TV')
        self._implementor.volume = 0


class iDevice(ABC):

    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, value: int) -> None: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    def power(self, value: bool) -> None: pass


class Television(iDevice):

    def __init__(self):
        self._volume = 50
        self._power = False

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, value: int) -> None:

        if not self.power:
            print('Turn the TV on')

        if value > 100 or value < 0:
            return

        self._volume = value
        print(f'Current volume: {self._volume}')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, value: bool) -> None:
        self._power = value
        print(f'The TV is {"on" if value else "off"}')


if __name__ == "__main__":
    tv = Television()
    remote = RemoteControl(tv)
    remote.volume_up()
    remote.power()
    remote.volume_up()

    remote2 = RemoteControlWithMute(tv)
    remote2.mute()
