from banco_de_dados import Banco_de_dados
from calculadora import Calculadora
from usuario import Usuario
from winy import Winy
from random import randint
    
banco_de_dados = Banco_de_dados()
calculadora = Calculadora()    
winy = Winy()

user = Usuario(winy.nome, winy.idade, winy.matricula)

banco_de_dados.adicionar_ao_dicionario('nome' , user.get_nome())
banco_de_dados.adicionar_ao_dicionario('idade', user.get_idade())
banco_de_dados.adicionar_ao_dicionario('matricula', user.get_matricula())

dicionario = banco_de_dados.get_dicionario()

def asteristico(num: int) -> str:
    for i in range(num):
        print('*' * (i + 1))
        i += 1
    

login = user.usuario_is_true('Yuri Winycius', 30297010)

if login is True:
    print('Entrou')

    cal = []

    for c in range(5):
        num1 = randint(1, 5)
        num2 = randint(6, 10)
        
        calculo = calculadora.calcular('+', num1, num2)
        cal.append(calculo)

    banco_de_dados.adicionar_ao_dicionario('calculo', cal)     

    for chave, valor in dicionario.items():
        print(f'{chave}: {valor}')

    asteristico(5)    
      

else:
    print('User or passaword wrong.')
           