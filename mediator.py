from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, componente1: Componente1, componente2: Componente2) -> None:
        self._componente1 = componente1
        self._componente1.mediator = self
        self._componente2 = componente2
        self._componente2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Netflix responde con lo siguiente:")
            self._componente2.do_c()
        elif event == "D":
            print("Netflix responde con lo siguiente:")
            self._componente1.do_b()
            self._componente2.do_c()


class Base:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class Componente1(Base):
    def do_a(self) -> None:
        print("Componente 1: Muestra perfiles")
        print("Cliente: Escoje un perfil.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Componente: Aplica el filtro.")
        self.mediator.notify(self, "B")


class Componente2(Base):
    def do_c(self) -> None:
        print("Componente 2: Muestra catálogo")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Componente 2: Carga el catálogo de series.")
        print("Cliente: Escoje series por 'Drama' ")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    c1 = Componente1()
    c2 = Componente2()
    mediator = ConcreteMediator(c1, c2)

    print("Cliente: Entra a Netflix")
    c1.do_a()

    print("\n", end="")

    print("Cliente: Selecciona 'Series'.")
    c2.do_d()