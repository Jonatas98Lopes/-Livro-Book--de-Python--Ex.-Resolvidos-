# Não há necessidade de escrita de algoritmo.
# A única alteração aqui, deve-se a quantidade de elementos que foi de 5 a 7.

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input("Qual a sua nota? "))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"Nota {x}: {notas[x]:5.2f}")
    x += 1
print(f"Média: {soma / x:5.2f}")
    

