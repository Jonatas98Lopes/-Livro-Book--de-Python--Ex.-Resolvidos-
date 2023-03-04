# Use função para definir se o primeiro número é múltiplo do segundo.

def multiplo(a, b):
    if a % b == 0:
        return True
    return False

a = int(input("Digite o primeiro número que deseja testar: "))
b = int(input("Digite o segundo número que deseja testar: "))
print(multiplo(a, b))