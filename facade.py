from __future__ import annotations


class Fachada:
    def __init__(self, calentarAgua: calentarAgua, molerCafe: molerCafe) -> None:
        self._calentarAgua = calentarAgua or calentarAgua()
        self._molerCafe = molerCafe or molerCafe()

    def operation(self) -> str:
        arr = []
        arr.append("Encendiendo cafetera:")
        arr.append(self._calentarAgua.proceso())
        arr.append(self._molerCafe.proceso())
        arr.append("--Espera--")
        arr.append(self._calentarAgua.terminado())
        arr.append(self._molerCafe.terminado())
        return "\n".join(arr)


class calentarAgua:
    def proceso(self) -> str:
        return "Cafetera: Calentando agua..."

    def terminado(self) -> str:
        return "Cafetera: Agua caliente."


class molerCafe:
    def proceso(self) -> str:
        return "Cafetera: Moliendo café..."

    def terminado(self) -> str:
        return "Cafetera: Café molido."


def usuario(fachada: Fachada) -> None:
    print(fachada.operation(), end="")


if __name__ == "__main__":
    calentarAgua = calentarAgua()
    molerCafe = molerCafe()
    fachada = Fachada(calentarAgua, molerCafe)
    usuario(fachada)
    print("\Café listo para servir")