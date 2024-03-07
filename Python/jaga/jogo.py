from random import randint

class Jogo:
    def __init__(self, usuario) -> None:
        self.__usuario = usuario
        return self.__jogar()
    
    def __jogar(self) -> str:
        print('Vamos jogar, você tem 5 chances.')

        num = randint(1, 10)

        for i in range(5):
            number = int(input('Adivinhe o número: '))

            if number == num:
                print('ACERTOU!')

            else:
                print('Tente novamente.') 
