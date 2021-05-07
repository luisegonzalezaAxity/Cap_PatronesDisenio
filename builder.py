from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Constructor(ABC):
    @abstractproperty
    def producto(self) -> None:
        pass

    @abstractmethod
    def producir_parteA(self) -> None:
        pass

    @abstractmethod
    def producir_parteB(self) -> None:
        pass

    @abstractmethod
    def producir_parteC(self) -> None:
        pass


class Creador1(Constructor):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._producto = Producto1()

    @property
    def producto(self) -> Producto1:
        producto = self._producto
        self.reset()
        return producto

    def producir_parteA(self) -> None:
        self._producto.add("3 botones")

    def producir_parteB(self) -> None:
        self._producto.add("DPI")

    def producir_parteC(self) -> None:
        self._producto.add("RGB")


class Producto1():
    def __init__(self) -> None:
        self.partes = []

    def add(self, part: Any) -> None:
        self.partes.append(part)

    def lista_partes(self) -> None:
        print(f"Componentes: {', '.join(self.partes)}", end="")


class Patron:
    def __init__(self) -> None:
        self._constructor = None

    @property
    def Constructor(self) -> Constructor:
        return self._Constructor

    @Constructor.setter
    def Constructor(self, constructor: Constructor) -> None:
        self._Constructor = constructor

    def build_minimal_viable_producto(self) -> None:
        self.Constructor.producir_parteA()

    def build_full_featured_producto(self) -> None:
        self.Constructor.producir_parteA()
        self.Constructor.producir_parteB()
        self.Constructor.producir_parteC()


if __name__ == "__main__":
    patron = Patron()
    Constructor = Creador1()
    patron.Constructor = Constructor

    print("Ratón básico: ")
    patron.build_minimal_viable_producto()
    Constructor.producto.lista_partes()

    print("\n")

    print("Ratón gama media: ")
    patron.build_full_featured_producto()
    Constructor.producto.lista_partes()

    print("\n")

    print("Ratón personalizado: ")
    Constructor.producir_parteA()
    Constructor.producir_parteB()
    Constructor.producto.lista_partes()