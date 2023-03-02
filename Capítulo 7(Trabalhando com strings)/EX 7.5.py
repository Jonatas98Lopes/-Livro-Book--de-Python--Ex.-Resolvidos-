# ADICIONANDO ELEMENTOS NÃO PRESENTES NA STRING_2:

string_1 = input("Digite um conjunto de caracteres: ")
string_2 = input("Digite outro conjunto de caracteres: ")
lista = []
for elemento in string_1:
    teste = string_2.find(elemento)
    if not(teste >= 0):
        lista.append(elemento)
resultado = "".join(lista)
print(resultado)