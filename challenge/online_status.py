statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(diccionario):
    x=0
    for llave in diccionario:
        if diccionario[llave]== "online":
            x+=1
    return x

print(online_count(statuses))
