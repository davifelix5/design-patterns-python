from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self):
        self.successor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandleABC(Handler):

    def __init__(self, successor: Handler):
        self.letters = ('A', 'B', 'C')
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'The class HandlerABC cold handle with the value {letter}'
        return self.successor.handle(letter)


class HandleDEF(Handler):

    def __init__(self, successor: Handler):
        self.letters = 'D', 'E', 'F'
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'The class HandlerDEF could handle with the value {letter}'
        return self.successor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'The value {letter} could not be handled in the chain'


if __name__ == "__main__":
    unsolved = HandlerUnsolved()
    second_handler = HandleDEF(unsolved)
    first_handler = HandleABC(second_handler)

    print(first_handler.handle('A'))
    print(first_handler.handle('D'))
    print(first_handler.handle('H'))
    print()
    print(second_handler.handle('D'))
