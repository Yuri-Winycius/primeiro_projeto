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

for itens in dicionario.values():
    print(itens)

if user.usuario_true('Yuri Winycius', 30297010) is True:
    print('Entrou')

else:
    print('User or passaword wrong.')