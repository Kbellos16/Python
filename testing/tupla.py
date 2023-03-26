tuples= tuple()
other_tuple=()
other_tuple= (23,34,56,67)
tuples= (38,1.86,'vieira', "jose")
print(tuples.index('vieira'))#indice donde se encuentra la variable
print(tuples.count('vieira'))#cantidad de variables con ese nombre
#tuples[1]= 30 no es alterable
sum_tupla= tuples+other_tuple
print(sum_tupla)
print(sum_tupla[3:6]) #te imprime del 3 al 5
tuples = list(tuples)#cambiarlo a lista
print(type(tuples))