from banco_de_dados import Banco_de_dados
from calculadora import Calculadora
from usuario import Usuario
from random import randint

class Matricula():
    def gerador_de_matricula(self) -> int:
        number_one = str(randint(100, 500))
        number_two = str(randint(501, 999))

        matricula = number_one + number_two
        return matricula
    
banco_de_dados = Banco_de_dados()
calculadora = Calculadora()    
main = Matricula()

matricula = main.gerador_de_matricula()

num1 = 7
num2 = 8
multiplicacao = calculadora.calcular('*', num1, num2)
calculo = [num1 ,num2 , multiplicacao]

winy = Usuario('Winycius', 20, matricula)
banco_de_dados.adicionar_ao_dicionario('usuario' , winy.get_usuario())
banco_de_dados.adicionar_ao_dicionario('calculos' , calculo)
print(banco_de_dados.get_dicionario())
banco_de_dados.remover_do_dicionario('calculos')
print(banco_de_dados.get_dicionario())
