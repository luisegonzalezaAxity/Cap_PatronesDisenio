from abc import ABC, abstractmethod


class Youtube(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class ObtenerVideos(Youtube):
    def request(self) -> None:
        print("--Recopilando los videos--")


class Proxy(Youtube):
    def __init__(self, descargar: ObtenerVideos) -> None:
        self._descargar = descargar

    def request(self) -> None:
        if self.validar_membresia():
            self._descargar.request()
            self.log_access()

    def validar_membresia(self) -> bool:
        print("Proxy: --Validando membresia Youtube--")
        return True

    def log_access(self) -> None:
        print("--Descargando videos--", end="")


def client_code(youtube: Youtube) -> None:
    youtube.request()


if __name__ == "__main__":
    print("Cliente: Entrando a Youtube...")
    descargar = ObtenerVideos()
    client_code(descargar)
    print("Videos generados")

    print("")

    print("Cliente: Quiero descargar estos videos")
    proxy = Proxy(descargar)
    client_code(proxy)