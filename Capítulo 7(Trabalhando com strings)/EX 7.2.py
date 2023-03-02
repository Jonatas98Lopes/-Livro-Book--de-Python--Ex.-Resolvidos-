# ENTRE DUAS STRINGS, ACHAR OS CARACTERES COMUNS:

string_1 = "AAACTBF"
string_2 = "CBT"
lista = []
for i in range(len(string_2)):
    igual = string_1.find(string_2[i])
    if igual >= 0:
        lista.append(string_2[i])
resultado = "".join(lista)
print(resultado)