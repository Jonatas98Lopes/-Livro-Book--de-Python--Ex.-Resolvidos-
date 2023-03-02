total = 0
while True:
    codigo = int(input("Digite o código do produto: "))
    if codigo == 0:
        print(f"Total a pagar: R$ {total:.2f}")
        break
    quantidade = int(input("Digite a quantidade desejada: "))
    if codigo == 1:
        total += quantidade * 0.50
    elif codigo == 2:
        total += quantidade * 1.00
    elif codigo == 3:
        total += quantidade * 4.00
    elif codigo == 5:
        total += quantidade * 7.00
    elif codigo == 9:
        total += quantidade * 8.00
    else:
        print("Código inválido")
