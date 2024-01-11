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

login = user.usuario_is_true('Yuri Winycius', 30297010)

if login is True:
    print('Entrou')

    part1 = calculadora.calcular('+', user.get_idade(), user.get_matricula())
    part2 = calculadora.calcular('/', part1, 5)
    banco_de_dados.adicionar_ao_dicionario('calculo', part2)

    print(dicionario)

else:
    print('User or passaword wrong.')
        
for chave, valor in dicionario.items():
    print(f'{chave}:')
    print(valor)        