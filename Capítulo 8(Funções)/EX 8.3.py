# Função que recebe um lado de um quadrado e retorna sua área.

def area(lado):
    return (lado ** 2)

a = int(input("Digite o valor de um lados do quadrado: "))
print(area(a))