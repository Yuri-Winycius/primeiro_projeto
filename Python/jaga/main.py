from banco_de_dados import Banco_de_dados
from calculadora import Calculadora
from usuario import Usuario
from random import randint

banco_de_dados = Banco_de_dados()
calculadora = Calculadora()
winy = Usuario('Yuri Winycius', 20, 12345)
clau = Usuario('Claudete', 38, 23456)

banco_de_dados.adicionar_a_lista(winy.nome)
banco_de_dados.adicionar_a_lista(winy.idade)
banco_de_dados.adicionar_a_lista(winy.get_matricula())
banco_de_dados.adicionar_a_lista('Resultados ->')

for c in range(0, 5):
    num1 = randint(1, 10)
    num2 = randint(1, 5)
    resultado = calculadora.calcular('*', num1 = num1, num2 = num2)
    banco_de_dados.adicionar_a_lista(resultado)
    c += 1

banco_de_dados.adicionar_a_lista(clau.nome)
banco_de_dados.adicionar_a_lista(clau.idade)
banco_de_dados.adicionar_a_lista(clau.get_matricula())
banco_de_dados.adicionar_a_lista('Resultados ->')


while True:
    num1 = randint(1, 10)
    num2 = randint(1, 5)
    resultado = calculadora.calcular('/', num1 = num1, num2 = num2)
    banco_de_dados.adicionar_a_lista(resultado)
    c += 1
    if c == 5:
        break

print(banco_de_dados.get_lista())