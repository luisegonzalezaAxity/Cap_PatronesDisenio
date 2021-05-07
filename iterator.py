from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class OrdenamientoAlfabetico(Iterator):
    _posicion: int = None
    _inversa: bool = False

    def __init__(self, coleccion: Coleccion, reverse: bool = False) -> None:
        self._coleccion = coleccion
        self._inversa = reverse
        self.posicion = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._coleccion[self.posicion]
            self.posicion += -1 if self._inversa else 1
        except IndexError:
            raise StopIteration()

        return value


class Coleccion(Iterable):
    def __init__(self, coleccion: List[Any] = []) -> None:
        self._coleccion = coleccion

    def __iter__(self) -> OrdenamientoAlfabetico:
        return OrdenamientoAlfabetico(self._coleccion)

    def get_inversa_iterator(self) -> OrdenamientoAlfabetico:
        return OrdenamientoAlfabetico(self._coleccion, True)

    def agregar_equipo(self, item: Any):
        self._coleccion.append(item)


if __name__ == "__main__":
    coleccion = Coleccion()
    coleccion.agregar_equipo("Top 1.- Cloud9")
    coleccion.agregar_equipo("Top 2.- Team liquid")
    coleccion.agregar_equipo("Top 3.- Faze clan")

    print("Los mejores equipos de la eSports:")
    print("\n".join(coleccion))
    print("")

    print("Comenzando por el top 3:")
    print("\n".join(coleccion.get_inversa_iterator()), end="")