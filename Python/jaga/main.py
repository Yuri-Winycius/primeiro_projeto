from banco_de_dados import Banco_de_dados
from calculadora import Calculadora
from usuario import Usuario
from winy import Winy
from jogo import Jogo
from random import randint
    
banco_de_dados = Banco_de_dados()
calculadora = Calculadora()    
winy = Winy()

user = Usuario(winy.nome, winy.idade, winy.matricula)

banco_de_dados.adicionar_ao_dicionario('nome' , user.get_nome())
banco_de_dados.adicionar_ao_dicionario('idade', user.get_idade())
banco_de_dados.adicionar_ao_dicionario('matricula', user.get_matricula())

dicionario = banco_de_dados.get_dicionario()

login = user.usuario_is_true('Yuri Winycius', 30297010)

if login is True:
    print('Entrou')

    cal = []

    for c in range(5):
        num1 = randint(1, 2)
        num2 = randint(3, 4)
        
        calculo = calculadora.calcular('+', num1, num2)
        cal.append(calculo)

    banco_de_dados.adicionar_ao_dicionario('calculo', cal)     

    jogo = Jogo(winy.nome, 2)    

else:
    print('User or passaword wrong.')
           