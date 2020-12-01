"""
SINGLETON
É um padrão de projeto de que permite a cdefinição de uma classe que não
pode ser instanciada mais de uma vez
Mesmo que instanciada em várias variáveis, só haverá uma classe singleton
"""


class AppSettings:
    """
    Nesse caso, se outra instância for chamada, os atributos serão redefinidos,
    o que pode gerar um programa
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Sempre retorna a mesma instância, que é criada caso ainda não exista
        """
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
