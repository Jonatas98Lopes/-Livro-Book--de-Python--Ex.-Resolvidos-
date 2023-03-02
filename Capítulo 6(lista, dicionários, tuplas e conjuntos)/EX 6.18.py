repeticoes = {}
frase = input("Qual a frase que deseja verificar? ")
for i in frase:         # Outra forma de simplificar este bloco é: repeticoes[i] = repeticoes.get(i, 0) + 1
    if i == " ":
        continue
    if i not in repeticoes:
        repeticoes[i] = 1
    else:
        repeticoes[i] += 1
print(repeticoes)