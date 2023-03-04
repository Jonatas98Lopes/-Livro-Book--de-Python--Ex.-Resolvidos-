# Usando for em vez de while no programa 8.2:

"""
def soma(L): Como não criar uma função eficiente:
    total = 0
    x = 0
    while x < 5: <- Veja que a função está definida para um tamanho de lista apenas, no caso com 5 posições.
        total += L[x]
    return total

L = [1,7,2,9,15]
print(soma(L))
print(soma([7,9,12,3,100,20,4]))
"""

def soma(L):
    total = 0
    for i in L:
        total += i
    return total


L = [1,7,2,9,15]
print(soma(L))
print(soma([7,9,12,3,100,20,4]))