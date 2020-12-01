def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'Tema Escuro'
        self.font = 'Arial, sans-sefif'


if __name__ == "__main__":
    instance1 = AppSettings()
    instance2 = AppSettings()

    instance1.tema = 'Tema Claro'
    # O tema é defenido como escuro, mas, por ser um singleto, ao mudar na
    # instância 1, ele também muda na instância 2
    print(instance2.tema)
