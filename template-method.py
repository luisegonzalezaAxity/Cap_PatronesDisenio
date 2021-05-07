from abc import ABC, abstractmethod


class Auto(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("Puerta: Yo construyo la puerta")

    def base_operation2(self) -> None:
        print("Llantas: Yo construyo las llantas ")

    def base_operation3(self) -> None:
        print("Volante: Yo construyo los volantes")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class JuntaDePiezas(Auto):
    def required_operations1(self) -> None:
        print("Nissan: Yo junto las puertas")

    def required_operations2(self) -> None:
        print("Nissan: Yo junto las llantas")


class Armado(Auto):
    def required_operations1(self) -> None:
        print("Yo implemento las puertas")

    def required_operations2(self) -> None:
        print("Armado del vehículo con puertas")

    def hook1(self) -> None:
        print("Armado del vehículo con llantas")


def client_code(abstract_class: Auto) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    print("Fábrica de autos:")
    client_code(JuntaDePiezas())
    print("")

    print("Misma fábrica con diferentes operaciones: ")
    client_code(Armado())