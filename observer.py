from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Canal(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Canal(Canal):
    _observers: List[Observer] = []
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Canal: Aumentanto o disminuyendo suscripciones...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nPersona: Se suscribe o desuscribe al canal.")
        self._state = randrange(0, 10)

        print(f"Creador: Mis suscriptores ahora son: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, canal: Canal) -> None:
        pass

class Observador1(Observer):
    def update(self, canal: Canal) -> None:
        if canal._state < 3:
            print("Canal: aumenta o disminuye suscriptores")


class Observador2(Observer):
    def update(self, canal: Canal) -> None:
        if canal._state == 0 or canal._state >= 2:
            print("Canal: aumenta o disminuye suscriptores")


if __name__ == "__main__":
    canal = Canal()

    observer_a = Observador1()
    canal.attach(observer_a)

    observer_b = Observador2()
    canal.attach(observer_b)

    canal.some_business_logic()
    canal.some_business_logic()

    canal.detach(observer_a)

    canal.some_business_logic()