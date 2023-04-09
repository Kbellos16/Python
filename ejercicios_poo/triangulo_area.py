#calculo del area de  un triangulo 
class Triangulo():
    def __init__(self):
        self.base = self.lectura("base")
        self.altura = self.lectura("altura")
        self.area = 0

    def lectura(self, descripcion):
        return int(input("Introduzca la %s: " %descripcion ))

    def calculoArea(self):
        self.area = self.base * self.altura
    
    def impresion(self):
        print('El área del triangulo es %i:'% self.area)

resultado = Triangulo()
#resultado.altura = resultado.lectura("altura")
#resultado.base = resultado.lectura("base")
resultado.calculoArea()
resultado.impresion()

