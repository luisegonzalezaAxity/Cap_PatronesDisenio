from __future__ import annotations
from abc import ABC, abstractmethod


class Solicitud:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Estado de la compra: {type(state).__name__}")
        self._state = state
        self._state.solicitud = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    @property
    def solicitud(self) -> Solicitud:
        return self._solicitud

    @solicitud.setter
    def solicitud(self, solicitud: Solicitud) -> None:
        self._solicitud = solicitud

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class EnCamino(State):
    def handle1(self) -> None:
        print("EnCamino: Fue entregado.")
        self.solicitud.transition_to(Entregado())

    def handle2(self) -> None:
        print("EnCamino handles request2.")


class Entregado(State):
    def handle1(self) -> None:
        print("Entregado handles request1.")

    def handle2(self) -> None:
        print("¡Gracias por su compra!")


if __name__ == "__main__":
    solicitud = Solicitud(EnCamino())
    solicitud.request1()
    solicitud.request2()