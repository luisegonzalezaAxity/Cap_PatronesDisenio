from __future__ import annotations
from abc import ABC, abstractmethod


class Industria(ABC):

    @abstractmethod
    def procesar_materia(self):

        pass

    def almacenar_materia(self) -> str:

        producto = self.procesar_materia()

        resultado = f"Se ha almacenado el producto en la industria {producto.operacion()}"

        return resultado

class Cocacola(Industria):

    def procesar_materia(self) -> Producto:
        return ProductoCocacola()


class SanRafael(Industria):
    def procesar_materia(self) -> Producto:
        return ProductoSanRafael()


class Producto(ABC):

    @abstractmethod
    def operacion(self) -> str:
        pass

class ProductoCocacola(Producto):
    def operacion(self) -> str:
        return "{Cocacola}"


class ProductoSanRafael(Producto):
    def operacion(self) -> str:
        return "{San Rafael}"


def empresa(industria: Industria) -> None:

    print(f"Se trabaja sobre el pedido. \n"
        f"{industria.almacenar_materia()}", end="")


if __name__ == "__main__":
    print("Se ha recibido el pedido en Cocacola.")
    empresa(Cocacola())
    print("\n")

    print("Se ha recibido el pedido en San Rafael.")
    empresa(SanRafael())