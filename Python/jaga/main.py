from banco_de_dados import Banco_de_dados
from calculadora import Calculadora
from usuario import Usuario
from matricula import Matricula
from random import randint
    
banco_de_dados = Banco_de_dados()
calculadora = Calculadora()    
main = Matricula()

matricula = main.gerador_de_matricula()
    
winy = Usuario('Winycius', 20, matricula)

banco_de_dados.adicionar_ao_dicionario('nome' , winy.get_nome())
banco_de_dados.adicionar_ao_dicionario('idade', winy.get_idade())
banco_de_dados.adicionar_ao_dicionario('matricula', winy.get_matricula())

dicionario = banco_de_dados.get_dicionario()

for itens in dicionario.values():
    print(itens)