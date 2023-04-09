'''Crear un programa que tenga una lista, luego crear una función 
con la cual se van a pedir números al usuario para agregar a la lista. 
Debes crear una segunda funcion en donde se ordenen los números 
pares e impares dentro de dos listas nuevas'''
lista = []
def registrar_numero():
    for i in range(6):
        numero = float(input('Agrege un número:\n'))
        lista.append(numero)
    return lista
registrar_numero()

def ordenar_par_impar():
    lista.sort()
    par = []
    impar = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i) 
    print('Números pares', par)
    print('Números impares', impar)

ordenar_par_impar()
