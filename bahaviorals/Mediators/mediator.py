from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime


class Colleague(ABC):

    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator: Mediator = mediator
        self.received_messages: List[Dict] = []
        self.mediator.add_colleague(self)

    @abstractmethod
    def receive_direct(self, sender_name: str, msg: str) -> None: pass

    @abstractmethod
    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.handle_direct(self, receiver, msg)

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    def __str__(self):
        return f'Person({self.name})'

    def __repr__(self):
        return self.__str__()


class Person(Colleague):

    def receive_direct(self, sender_name: str, msg: str) -> None:
        """
        O mediador enviar o direct de volta para pessoas
        """
        print(f'{sender_name} said to {self.name}: {msg}')

    def send_direct(self, receiver: str, msg: str) -> None:
        """
        O direct pe enviado para o mediador
        """
        self.mediator.handle_direct(self, receiver, msg)

    def broadcast(self, msg: str) -> None:
        """
        O broadcast é enviado para o mediador, que printa a mensagem na tela
        """
        self.mediator.handle_broadcast(self, msg)


class Mediator(ABC):

    @abstractmethod
    def add_colleague(self, colleague: Colleague) -> None: pass

    @abstractmethod
    def handle_broadcast(self, person: Colleague, msg: str) -> None: pass

    @abstractmethod
    def handle_direct(
        self, sender: Colleague, receiber: str, msg: str) -> None: pass


class ChatRoom(Mediator):
    def __init__(self):
        self.colleagues: List[Colleague] = []

    def add_colleague(self, colleague: Colleague) -> None:
        self.colleagues.append(colleague)

    def remove_colleague(self, colleague: Colleague) -> None:
        self.colleagues.remove(colleague)

    def handle_broadcast(self, person: Colleague, msg: str) -> None:

        for colleague in self.colleagues:
            if colleague != person:
                colleague.received_messages.append(
                    {'time': datetime.now(), 'sender': person, 'msg': msg})

        print(f'{person.name} says: {msg}')

    def handle_direct(
            self, sender: Colleague, receiver: str, msg: str) -> None:

        receivers: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        receiver_obj = receivers[0] if receivers else None

        if not receiver_obj or receiver_obj == sender:
            return

        receiver_obj.received_messages.append(
            {
                'time': datetime.now(),
                'sender': sender,
                'msg': msg,
                'direct': True
            }
        )

        receiver_obj.receive_direct(sender.name, msg)


if __name__ == "__main__":
    chat = ChatRoom()
    c1 = Person('Davi', chat)
    c2 = Person('Carla', chat)
    c3 = Person('Joana', chat)

    c1.broadcast('Hey there')
    c2.broadcast("Hey, How are y'all?")
    c3.broadcast('Fine. What about you guys?')

    print()

    c3.send_direct('Carla', "Hey there, let's hang out someday")
    c2.send_direct('Joana', "I'd love to!")

    print()

    print(c1.received_messages)
    print(c2.received_messages)
    print(c3.received_messages)
