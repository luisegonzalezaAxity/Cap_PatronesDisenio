from __future__ import annotations
from abc import ABC, abstractmethod


class TecladoMem:
    def __init__(self, caracteristica: Caracteristica) -> None:
        self.caracteristica = caracteristica

    def operacion(self) -> str:
        return (f"Teclado membrana:\n"
                f"{self.caracteristica.descripcion()}")


class TecladoMec(TecladoMem):
    def operacion(self) -> str:
        return (f"Teclado mecánico\n"
                f"{self.caracteristica.descripcion()}")


class Caracteristica(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass

class CaracteristicaMem(Caracteristica):
    def descripcion(self) -> str:
        return "El tecladoMem de membrana es de menor duración."


class CaracteristicaMec(Caracteristica):
    def descripcion(self) -> str:
        return "El tecladoMec mecánico es de mayor duración."


def interesado(tecladoMem: TecladoMem) -> None:
    print(tecladoMem.operacion(), end="")


if __name__ == "__main__":
    caracteristica = CaracteristicaMem()
    tecladoMem = TecladoMem(caracteristica)
    interesado(tecladoMem)

    print("\n")

    caracteristica = CaracteristicaMec()
    tecladoMem = TecladoMec(caracteristica)
    interesado(tecladoMem)