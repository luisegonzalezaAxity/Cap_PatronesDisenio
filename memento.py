from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class LlaveOriginal():
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Codificación inicial: {self._state}")

    def do_something(self) -> None:
        print("--Actualizando versión...--")
        self._state = self._generate_random_string(30)
        print(f"La nueva codificación es: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"La codificación a cambiado a: {self._state}")


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    def __init__(self, llaveOriginal: LlaveOriginal) -> None:
        self._mementos = []
        self._originator = llaveOriginal

    def backup(self) -> None:
        print("\n--Guardando versión--")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Restaurando versión a: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Aquí tienes la lista de cambios:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    llaveOriginal = LlaveOriginal("123Cod3C.")
    caretaker = Caretaker(llaveOriginal)

    caretaker.backup()
    llaveOriginal.do_something()

    caretaker.backup()
    llaveOriginal.do_something()

    caretaker.backup()
    llaveOriginal.do_something()

    print()
    caretaker.show_history()

    print("\nCliente: Volvamos a codificaciones anteriores\n")
    caretaker.undo()