# Quantas vezes o caractere aparece:

string_1 = "TTAAC"
resultado = {}
for i in string_1:
    if i not in resultado:
        resultado[i] = string_1.count(i)

print(resultado)