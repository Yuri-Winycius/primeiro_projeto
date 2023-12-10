from banco_de_dados import Banco_de_dados
from calculadora import Calculadora
from usuario import Usuario
from random import randint

banco_de_dados = Banco_de_dados()
calculadora = Calculadora()
class Matricula():
    def gerador_de_matricula(self) -> int:
        number_one = randint(100, 500)
        number_two = randint(501, 999)

        number_one = str()
        number_two = str()

        matricula = number_one + number_two
        return matricula
    
main = Matricula() 
matricula = main.gerador_de_matricula()
print(matricula)

winy = Usuario('Winycius', 20, matricula)
banco_de_dados.adicionar_a_lista(winy.get_usuario())
print(banco_de_dados.get_lista())
