# 1:  X | O | X      "C1"= row=0 colum=2 (0,2)
#    -----------
# 2:    |   |        "A3"  row=3 colum=0 (2,0)
#    -----------
# 3:  O |   |

#     A   B  C

def get_row_col(direction):
    dire_up=direction.upper()  
    lista=[]
    diccionario={'A':0,'B':1,'C':2,'1':0,'2':1,'3':2}
    for i in dire_up:
        lista.append(diccionario[i])
    lista.reverse()
    tupla=tuple(lista)
    return tupla


print(get_row_col('a3'))