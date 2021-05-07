from __future__ import annotations
from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def ejecutar(self) -> None:
        pass


class Atajos(Comando):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def ejecutar(self) -> None:
        print(f"Comando: Yo mantendré guardado tu texto copiado."
            f"({self._payload})")


class CopiadoPegado(Comando):
    def __init__(self, so: SO, a: str, b: str) -> None:
        self._so = so
        self._a = a
        self._b = b

    def ejecutar(self) -> None:
        print("Comando: Ctrl + v", end="")
        self._so.do_something(self._a)
        self._so.do_something_else(self._b)


class SO:
    def do_something(self, a: str) -> None:
        print(f"\nSO: Trabajando en ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nSO: Trabajando en ({b}.)", end="")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, comando: Comando):
        self._on_start = comando

    def set_on_finish(self, comando: Comando):
        self._on_finish = comando

    def accion(self) -> None:
        print("Estudiante: Comenzaré a escribir mi tesis.")
        if isinstance(self._on_start, Comando):
            self._on_start.ejecutar()

        print("Estudiante: ...escribiendo su tesis...")

        print("Estudiante: Necesito pegar lo que copié.")
        if isinstance(self._on_finish, Comando):
            self._on_finish.ejecutar()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(Atajos("Ctrl + c"))
    so = SO()
    invoker.set_on_finish(CopiadoPegado(
        so, "Guardar como PDF", "Guardar en: \\user\\documentos"))

    invoker.accion()