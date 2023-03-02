T = [-10, -8, 0, 1, 2, 5, -2, -4]
minimo = T[0]
maximo = T[0]
soma = 0
for e in T:
    soma += e
    if e > maximo:
        maximo = e
    if e < minimo:
        minimo = e

print(f"Valor máximo é: {maximo}")
print(f"Valor mínimo é: {minimo}")
print(f"A média de temperatura é: {soma / len(T)}")
