a= 'HeLlO'
def capital_indexes(a):
    b=[]
    for i in range(0, len(a)):
        if a[i]==a[i].capitalize():
            b.append(i)
    print(b)

capital_indexes(a)
