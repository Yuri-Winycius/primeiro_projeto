class Calculadora:
    def calcular(self, op, num1: int, num2: int):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        elif op == '/':
            return self.__dividir(num1, num2)
        elif op == '*':
            return self.__multiplicar(num1, num2)
        else:
            print('Operação invalida!')        

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2        
    
    def __dividir(self, num1, num2) -> float:
        return num1 / num2 
    
    def __multiplicar(self, num1, num2) -> int:
        return num1 * num2
    