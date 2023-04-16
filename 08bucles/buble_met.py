# metodo de la burbuja consiste en un metod que se usa para ordenar una lista
def burble_met(lista):
    
    n= int(len(lista))
    for i in range(n-1):
        for j in range(n-1-i): 
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista
print(burble_met(['e','t','g','s']))






