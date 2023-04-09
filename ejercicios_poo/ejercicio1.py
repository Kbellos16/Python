# Ejercicio 1
# Realizar un programa que conste de una clase llamada Estudiante,
# que tenga como atributos el nombre y la nota del alumno. Definir 
# los métodos para inicializar sus atributos, imprimirlos y mostrar 
# un mensaje con el resultado de la nota y si ha aprobado o no

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        self.Mensaje()

    def Mensaje(self):  
        if self.nota >= 10:
            self.mensaje = "aprobó la materia"
        else:
            self.mensaje = "reprobó"

alumno = Estudiante("Andres", 10)

print('El alumno {}, {} con una nota de {}'.format(alumno.nombre, alumno.mensaje, alumno.nota))

