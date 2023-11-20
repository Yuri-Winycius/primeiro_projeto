class Banco_de_dados:
    def __init__(self) -> None:
        self.__lista = []

    def adicionar_a_lista(self, lista: str) -> list:
        self.__set_lista(lista)
        self.get_lista()

    def get_lista(self) -> list:
        return self.__lista
    
    def __set_lista(self, lista: str) -> None:
        self.__lista.append(lista)
        
    def remover_da_lista(self, inde: int) -> list:
        self.__lista.pop(inde)
        return self.__lista