from random import randint

class Jogo:
    def __init__(self, usuario) -> None:
        self.__usuario = usuario
        return self.__jogar(self.__usuario)
    
    def __jogar(self, usuario) -> str:
        print('Vamos jogar, você tem 5 chances.')

        num = randint(1, 10)

        for i in range(5):
            number = int(input('Adivinhe o número: '))

            if number == num:
                print(f'ACERTOU {usuario}!')

            else:
                print(f'Tente novamente {usuario}.') 
