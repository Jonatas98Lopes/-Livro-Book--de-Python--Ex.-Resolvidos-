string_1 = "CTA"
string_2 = "ABC"
lista = []
for i in range(len(string_2)):
    igual = string_1.find(string_2[i])
    if not(igual >= 0):
        lista.append(string_2[i])

for i in range(len(string_1)):
    igual2 = string_2.find(string_1[i])
    if not(igual2 >= 0):
        lista.append(string_1[i])
resultado = "".join(lista)
print(resultado)

