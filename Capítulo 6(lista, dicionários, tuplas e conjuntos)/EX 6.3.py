lista = [12, 324, 354, 12, 34, 55, 34]
lista2 = [342, 55, 235, 255, 687, 32]
resultado = []
resultado.extend(lista)  # resultado = resultado + lista
x = 0
while x < len(lista2):
    if lista2[x] not in resultado:
        resultado.append(lista2[x])
    x += 1
print(resultado)
