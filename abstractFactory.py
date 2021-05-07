from __future__ import annotations
from abc import ABC, abstractmethod


class Local(ABC):
    @abstractmethod
    def tomar_orden(self) -> Producto1:
        pass

    @abstractmethod
    def agregar_complemento(self) -> Producto2:
        pass


class PizzaHut(Local):

    def tomar_orden(self) -> Producto1:
        return Orden1()

    def agregar_complemento(self) -> Producto2:
        return Producto2()


class Dominos(Local):

    def tomar_orden(self) -> Producto1:
        return Orden2()

    def agregar_complemento(self) -> Producto2:
        return ConcreteProductB2()


class Producto1(ABC):

    @abstractmethod
    def numero_orden(self) -> str:
        pass

class Orden1(Producto1):
    def numero_orden(self) -> str:
        return "Orden 1"


class Orden2(Producto1):
    def numero_orden(self) -> str:
        return "Orden 2"


class Producto2(ABC):
    @abstractmethod
    def tomando_orden(self) -> None:
        pass

    @abstractmethod
    def preparar_orden(self, trabajador: Producto1) -> None:
        pass

class Producto2(Producto2):
    def tomando_orden(self) -> str:
        return "Agregando una pizza a la orden."

    def preparar_orden(self, trabajador: Producto1) -> str:
        result = trabajador.numero_orden()
        return f"Resultado de trabajar con la orden: ({result})"


class ConcreteProductB2(Producto2):
    def tomando_orden(self) -> str:
        return "Agregando un refresco a la orden."

    def preparar_orden(self, trabajador: Producto1):
        result = trabajador.numero_orden()
        return f"El resultado de trabajar con la segunda orden ({result})"


def local(local: Local) -> None:
    productoA = local.tomar_orden()
    productoB = local.agregar_complemento()

    print(f"{productoB.tomando_orden()}")
    print(f"{productoB.preparar_orden(productoA)}", end="")


if __name__ == "__main__":
    print("Cliente: Me gustaría ordenar uan pizza:")
    local(PizzaHut())

    print("\n")

    print("Cliente: También me gustaría agregar un refresco:")
    local(Dominos())