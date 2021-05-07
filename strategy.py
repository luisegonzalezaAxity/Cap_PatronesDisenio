from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Problema():
    def __init__(self, estrategia: Estrategia) -> None:
        self._estrategia = estrategia

    @property
    def estrategia(self) -> Estrategia:
        return self._estrategia

    @estrategia.setter
    def estrategia(self, estrategia: Estrategia) -> None:
        self._estrategia = estrategia

    def hacer_solucion(self) -> None:
        result = self._estrategia.solucion(["a", "b", "c", "d", "e"])
        print(",".join(result))

class Estrategia(ABC):
    @abstractmethod
    def solucion(self, data: List):
        pass

class ConcreteStrategyA(Estrategia):
    def solucion(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Estrategia):
    def solucion(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    problema = Problema(ConcreteStrategyA())
    print("Niño: Mamá, necesito desordenar estas letras y comenzar por la e.")
    problema.hacer_solucion()
    print()

    print("Mamá: Así es como se tiene que hacer: ")
    problema.estrategia = ConcreteStrategyB()
    problema.hacer_solucion()