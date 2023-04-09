# Crear una clase Fabrica que tenga los atributos de Llantas, 
# Color y Precio; luego crear dos clases mas que hereden de Fabrica,
# las cuales son Moto y Carro. Crear metodos que muestren la cantidad 
# de llantas, color y precio de ambos transportes. Por ultimo, crear objetos
# para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica():
    def __init__(self, llantas, color, precio, objeto):
        self.llantas = llantas
        self.color = color
        self.precio = precio
        self.objeto = objeto
    def imprimir(self):
        print('La cantidad de llantas para %s es de %i unidades'%(self.objeto, self.llantas))
        print('El color de %s es %s'%(self.objeto, self.color))
        print('El precio es de %i' %self.precio)

class Moto(Fabrica):
    pass
class Carro(Fabrica):
    pass

moto = Moto(10, 'azul', 5000, "la moto")
moto.imprimir()