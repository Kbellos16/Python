# Write a function that takes a list of lists and flattens it into a one-dimensional list.
# Name your function flatten. It should take a single parameter and return a list.
# For example, calling:
# flatten([[1, 2], [3, 4]]) Should return the list: [1, 2, 3, 4]
flatten_list=[[1, 2], [3, 4],[9,0]]

def flatten(flatten_list):
    new_list=[]
    for i in range(0, len(flatten_list)):
        new_list+= (flatten_list[i])
        
    return new_list

print(flatten(flatten_list))