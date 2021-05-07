class Componente():
    def operacion(self) -> str:
        pass

class HeadSet(Componente):
    def operacion(self) -> str:
        return "AstroA50"

class Decorador(Componente):
    _componente: Componente = None

    def __init__(self, componente: Componente) -> None:
        self._componente = componente

    @property
    def componente(self) -> str:
        return self._componente

    def operacion(self) -> str:
        return self._componente.operacion()


class Stand(Decorador):
    def operacion(self) -> str:
        return f"StandRGB({self.componente.operacion()})"


class CargaInalmabrica(Decorador):
    def operacion(self) -> str:
        return f"Carga inalámbrica({self.componente.operacion()})"


def pedido(componente: Componente) -> None:
    print(f"Componente: {componente.operacion()}", end="")

if __name__ == "__main__":
    simple = HeadSet()
    print("Tengo un headset inalámbrico.")
    pedido(simple)
    print("\n")

    componente1 = Stand(simple)
    componente2 = CargaInalmabrica(componente1)
    print("Cliente: Me gustaría un stand para mi headset.")
    pedido(componente2)