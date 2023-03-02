from random import randint

def  gera_lista(qtd_elementos, vmin=1, vmax=100):
    L = []
    for i in range(qtd_elementos):
        L.append(randint(vmin, vmax))
    return L


lista = gera_lista(20)
lista2 = gera_lista(20)
conjunto = set(lista)
conjunto2 = set(lista2)

print(conjunto & conjunto2)
print(conjunto - conjunto2)
print(conjunto2 - conjunto)
print(conjunto ^ conjunto2)
print(conjunto - conjunto2)

