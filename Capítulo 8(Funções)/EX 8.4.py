# Escreva uma função que recebe a base e a altura de um triângulo e calcule sua área.

def area_triangulo(base, altura):
    return (base * altura) / 2

base = int(input("Digite a base do seu triângulo: "))
altura = int(input("Digite a altura do seu triângulo: "))
print(area_triangulo(base, altura))