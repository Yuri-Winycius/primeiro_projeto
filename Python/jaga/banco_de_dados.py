class Banco_de_dados:
    def __init__(self) -> None:
        self.__dicionario = {}

    def adicionar_ao_dicionario(self, chave: str, valor: str) -> dict:
        self.__set_dicionario(chave, valor)
        self.get_dicionario()

    def get_dicionario(self) -> dict:
        return self.__dicionario
    
    def __set_dicionario(self, chave: str, valor: str) -> None:
        self.__dicionario[chave] = valor
        
    def remover_do_dicionario(self, chave) -> list:
        del self.__dicionario[chave]
        return self.get_dicionario()