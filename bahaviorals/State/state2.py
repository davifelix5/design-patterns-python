from __future__ import annotations
from abc import ABC, abstractmethod


class PlayMode(ABC):

    def __init__(self, radio: MusicPlayer) -> None:
        self.radio = radio

    @abstractmethod
    def next_btn(self) -> None: pass

    @abstractmethod
    def previous_btn(self) -> None: pass

    @abstractmethod
    def handle_change_mode(self) -> None: pass


class RadioMode(PlayMode):

    def next_btn(self) -> None:
        print('Going to next radio station')
        self.radio.playing += 1000

    def previous_btn(self) -> None:

        if self.radio.playing == 0:
            return

        print('Going to previous radio station')
        self.radio.playing -= 1000

    def handle_change_mode(self) -> None:
        self.radio.playing = 1
        self.radio.play_mode = UBSMode(self.radio)


class UBSMode(PlayMode):

    def next_btn(self) -> None:
        print('Passing to next sound')
        self.radio.playing += 1

    def previous_btn(self) -> None:

        if self.radio.playing == 1:
            return

        print('Passing to previous sound')
        self.radio.playing += 1

    def handle_change_mode(self) -> None:
        self.radio.playing = 0
        self.radio.play_mode = RadioMode(self.radio)


class MusicPlayer:

    def __init__(self) -> None:
        self.play_mode: PlayMode = RadioMode(self)
        self.playing = 0

    def press_next(self):
        self.play_mode.next_btn()

    def press_previous(self):
        self.play_mode.previous_btn()

    def change_mode(self):
        self.play_mode.handle_change_mode()

    def __str__(self):
        return f'Playing {self.playing}'


if __name__ == "__main__":
    player = MusicPlayer()
    player.press_next()
    player.press_next()
    player.press_previous()
    print(player)
    print()
    player.change_mode()
    player.press_next()
    player.press_next()
    player.press_next()
    print(player)
