#The built-in zip function "zips" two lists. Write your own implementation of this function.

#Define a function named zap. The function takes two parameters, a and b. These are lists.

#Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.

#You may assume a and b have equal lengths.

#If you don't get it, think of a zipper

a=[0, 1, 2, 3]

b=[5, 6, 7, 8]

def zap(a,b):
    c=[]

    for i in range(0,len(a)):
        lista=(a[i],b[i])
        c.append(lista)
    return(c)
print(zap(a,b))

#def zap(a, b):
#    return [(a[i], b[i]) for i in range(len(a))]