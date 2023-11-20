class Usuario:
    def __init__(self, nome: str, idade: int, matricula: int) -> None:
        self.nome = nome
        self.idade = idade
        self.__matricula = matricula

    def get_matricula(self) -> int:
        return self.__matricula