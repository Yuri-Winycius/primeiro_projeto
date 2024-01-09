class Usuario:
    def __init__(self, nome: str, idade: int, matricula: int) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    def get_matricula(self) -> int:
        return self.__matricula
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_idade(self) -> str:
        return self.__idade