class SingletonMeta(type):
    instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instancias:
            instancia = super().__call__(*args, **kwargs)
            cls.instancias[cls] = instancia
        return cls.instancias[cls]


class Singleton(metaclass=SingletonMeta):
    def accion(self):
        pass


if __name__ == "__main__":
    # The client code.

    v1 = Singleton()
    v2 = Singleton()

    if id(v1) == id(v2):
        print("Singleton funciona, ambas variables contienen el mismo id de memoria.")
    else:
        print("Singleton falló, las variables no tienen el mismo id de memoria.")