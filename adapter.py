class Objetivo:
    def descifrador(self) -> str:
        return "Introduzca el código."

class Validador:
    def specific_descifrador(self) -> str:
        return ".setram :añesartnoC"
        


class Desencriptador(Objetivo, Validador):
    def descifrador(self) -> str:
        return f"Desencriptador: (Completado, la contraseña es:) {self.specific_descifrador()[::-1]}"


def client_code(objetivo: "Objetivo") -> None:
    print(objetivo.descifrador(), end="")


if __name__ == "__main__":
    print("Aventurero: Necesito descifrar un código \n")
    objetivo = Objetivo()
    client_code(objetivo)
    print("\n")

    validador = Validador()
    print(f"Validador: {validador.specific_descifrador()}", end="\n\n")

    desencriptador = Desencriptador()
    client_code(desencriptador)