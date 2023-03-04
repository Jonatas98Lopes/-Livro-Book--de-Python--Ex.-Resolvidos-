# SUBSTITUIÇÃO DE CARACTERES, QUANDO OS MESMOS SÃO ENCONTRADOS NA SEGUNDA, PELOS DA TERCEIRA:

string_1 = input("Digite um conjunto de caracteres: ")
string_2 = input("Digite outro conjunto de caracteres: ")
string_3 = input("Digite outro conjunto de caracteres: ")
lista = []
for elemento in string_1:
    teste = string_2.find(elemento)
    if not(teste >= 0):
        lista.append(elemento)
    else:
        lista.append(string_3[teste])
resultado = "".join(lista)
print(resultado)