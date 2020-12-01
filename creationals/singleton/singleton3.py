class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Escuro'
        self.font = 'Helvetica, sans serif'


if __name__ == "__main__":
    app1 = AppSettings()
    app2 = AppSettings()

    app1.tema = 'Claro'
    print(app2.tema)
