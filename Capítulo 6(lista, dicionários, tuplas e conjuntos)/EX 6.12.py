# Mudança do exemplo dado, no qual se procrura o maior número da lista.
L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)
