L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
primeiro = ''
x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posição {x}")
        if primeiro == '':
            print(f"O valor {p} foi achado primeiro")
            primeiro = 'p'
    if L[x] == v:
        print(f"{v} achado na posição {x}")
        if primeiro == '':
            print(f"O valor {v} foi achado primeiro")
            primeiro = 'v'
    x += 1
if primeiro == '':
    print(f"Ambos, {p} e {v}, não foram encontrados.")
