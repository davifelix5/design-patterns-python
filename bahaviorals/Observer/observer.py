"""
OBSERVER
Relação de um para muitos que promove mudanças nos objetos
dependetes (observer) quando o obejto observable é alterado
Ou o observer pode pegar os dados do absevable (push)
Ou o observable pode dar os dados para o observer (pull)
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class iObserver(ABC):

    @abstractmethod
    def update(self) -> None: pass


class iObservable(ABC):

    @abstractmethod
    def add_observer(self, observer: iObserver) -> None: pass

    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def remove_observer(self, observer: iObserver) -> None: pass

    @abstractmethod
    def reset_state(self, observer: iObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeatherStation(iObservable):

    def __init__(self):
        self._observer_collection: List[iObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = dict(**self._state, **state_update)

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: iObserver) -> None:
        self._observer_collection.append(observer)

    def remove_observer(self, observer) -> None:
        if observer in self._observer_collection:
            self._observer_collection.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observer_collection:
            observer.update()


class Smartphone(iObserver):
    def __init__(self, name: str, observable: iObservable, specs: Dict = None):
        self.name = name
        self._observable = observable
        self._state = {} if specs is None else specs
        self._observable.add_observer(self)

    @property
    def state(self):
        return self._state

    def update(self) -> None:
        self.state['wheater_info'] = self._observable.state


if __name__ == "__main__":
    station = WeatherStation()
    smartphone1 = Smartphone('Galaxy J5', station, {'Android': '4.1'})
    smartphone2 = Smartphone('Note 10', station, {'Android': '5.1'})
    smartphone3 = Smartphone('iPhone 8', station)

    station.state = {'temperature': '80 °F'}
    station.state = {'umidity': '65%'}

    print(smartphone1.state)
    print(smartphone2.state)
    print(smartphone3.state)
