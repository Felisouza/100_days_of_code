#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b.

# Exemple ► array_diff([1,2],[1]) == [2]

def array_diff(a, b):
    #your code here
    lista = []
    for i in a:
        if i not in b:
            lista.append(i)
    return lista

array_diff([1,2,2,3],[2])
