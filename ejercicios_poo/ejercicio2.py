# Realizar un programa en el cual, se declaren dos valores enteros por teclado 
# utilizando el método __init__. Calcular después la suma, resta, multiplicación
# y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
# Llamar a la clase Calculadora

class Calculadora():
    def __init__(self):
        self.valor_a = 0
        self.valor_b = 0
        self.operador = ''

    def leer_valores(self):
        self.valor_a = int(input('introduzca un primer valor: '))
        self.valor_b = int(input('introduzca un segundo valor: '))
    
    def leer_operador(self):
        self.operador = input('introduzca operación +, -, *, /: ')

    def suma(self):
        return self.valor_a + self.valor_b
    
    def resta (self):
        return self.valor_a - self.valor_b
    def multiplicar(self):
        return self.valor_a * self.valor_b
    def dividir(self):
        return self.valor_a / self.valor_b

    def operacion(self):
        if self.operador == '+':
            print(self.suma())
        elif self.operador=='-':
            print(self.resta())
        elif self.operador=='*':
            print(self.multiplicar())
        elif self.operador=='/':
            print(self.dividir())
        else:
            print('operación invalida')

calc = Calculadora()
calc.leer_valores()
calc.leer_operador()
calc.operacion()