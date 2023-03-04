# Use uma função para achar o maior de dois números:

def maior(a, b):
    if a > b:
        return a
    return b

a = int(input("Digite o primeiro número que deseja testar: "))
b = int(input("Digite o segundo número que deseja testar: "))
print(maior(a, b))
