from random import randint

class Matricula():
    def gerador_de_matricula(self) -> int:
        number_one = str(randint(100, 500))
        number_two = str(randint(501, 999))

        matricula = number_one + number_two
        return matricula