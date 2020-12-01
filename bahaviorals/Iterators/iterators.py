from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List, Any


class MyList(Iterable):

    def __init__(self) -> None:
        self._items: List[Any] = []

    def add(self, value: Any):
        self._items.append(value)

    def __iter__(self):
        return NormalIterator(self._items)

    def iter_backwards(self):
        return BackwardsIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


class NormalIterator(Iterator):

    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index == len(self._collection):
            raise StopIteration
        item = self._collection[self._index]
        self._index += 1
        return item


class BackwardsIterator(Iterator):

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = len(self._collection) - 1

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        item = self._collection[self._index]
        self._index -= 1
        return item


if __name__ == "__main__":
    my_list = MyList()
    my_list.add(1)
    my_list.add('Davi')
    my_list.add('Clovis')

    print(f'Minha lista: {my_list}')

    print('-=-'*15)

    print('Normal iterator')
    for item in my_list:
        print(item)

    print('-=-'*15)

    print('Itarating backwards')
    for item in my_list.iter_backwards():
        print(item)
