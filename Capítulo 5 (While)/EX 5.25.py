'''n = float(input("Qual o número do qual deseja obter a raiz quadrada? "))
b = 2
while True:
    if abs(n - (b * b)) <=0.0001:
        print(f"{n} ao quadrado equivale à {p}")
        break
    p = (b + (n / b) / 2)
    b = p
    
'''

n = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}")
