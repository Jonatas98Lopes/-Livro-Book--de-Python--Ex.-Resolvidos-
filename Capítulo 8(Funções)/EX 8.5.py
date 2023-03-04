# Reescrevendo o programa 8.1 utlizando métodos de pesquisa:

"""Programa anterior:

def pesquise(lista,  valor):
    for x, e in enumarate(lista):
         if e == valor:
            return x
    return None

L = [10,20,25,30]

print(pesquise(L, 25)) -> 2
print(pesquise(L, 27)) -> None
"""

def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return f"{valor} não está em {lista}"

L = [10,20,25,30]
print(pesquise(L, 25))
print()
print(pesquise(L, 27))

