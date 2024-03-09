from random import randint

class Jogo:
    def __init__(self, usuario: str, num: int) -> None:
        self.__usuario = usuario
        num = int(input('Escolha uma opção:'))
        print('1) Adivinhar')
        print('2) Asteristicos')

        if num == 1:
            return self.__jogar(usuario)
        
        if num ==2:
            return self.__asteristico(num, usuario)
    
    def __jogar(self, usuario: str) -> str:
        print('Vamos jogar, você tem 5 chances.')

        num = randint(1, 10)

        for i in range(5):
            number = int(input('Adivinhe o número: '))

            if number == num:
                print(f'ACERTOU {usuario}!')

            else:
                print(f'Tente novamente {usuario}.') 

    def __asteristico(self, num: int, usuario: str) -> str:
        for i in range(num):
            print(f'{usuario} ' * (i + 1))
            i += 1
                
