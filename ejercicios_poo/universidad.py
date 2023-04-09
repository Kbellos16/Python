# Crear un programa con tres clases 
#Universidad, con atributos nombre(Donde se almacena el nombre de la Universidad).
# Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante)
# Una ultima llamada Estudiante, que tenga como atributos su nombre y edad.
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con 
# un objeto llamado persona.

class Universidad():
    def __init__ (self,nombre_uni):
        self.nombre_uni= nombre_uni
        
    
class Carrera():
    def carrera(self,especialidad):
        self.especialidad=especialidad
        

class Estudiante (Universidad,Carrera):
    def informacion(self,nombre,edad):
        self.nombre = nombre 
        self.edad = edad
        print('Mi nombre es %s, mi edad es %s, estudio en la %s la carrera de %s'%(self.nombre,self.edad,self.nombre_uni,self.especialidad))
persona=Estudiante('UCV',)
persona.carrera("sitemas")
persona.informacion('Jose',20)
        