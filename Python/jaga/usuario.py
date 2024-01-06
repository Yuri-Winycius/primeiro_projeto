class Usuario:
    def __init__(self, nome: str, idade: int, matricula: int) -> None:
        self.nome = nome
        self.idade = idade
        self.__matricula = matricula

    def get_matricula(self) -> int:
        return self.__matricula
    
    def get_usuario(self) -> dict:
        return {'user': self.nome, 
                'age': self.idade,
                'matricula': self.get_matricula()}