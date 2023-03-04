ultimo = 10
ultimo2 = 200
fila = list(range(1, ultimo + 1))
fila2 = list(range(100, ultimo2 + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"\nExistem {len(fila2)} clientes na fila")
    print(f"Fila2 atual: {fila2}")
    print(f"Para Fila: Digite F para adicionar um cliente ao fim da lista,")
    print("ou A para realizar o atendimento. S para sair")
    print(f"Para Fila2: Digite G para adicionar um cliente ao fim da lista,")
    print("ou B para realizar o atendimento. S para sair")
    operacao = input("Operacao (F, G, A, B ou S):")
    x = 0
    while x < len(operacao):
        if operacao[x] in "Aa":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] in "Bb":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] in "Ff":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] in "Gg":
            ultimo2 += 1
            fila2.append(ultimo2)
        elif operacao[x] in "Ss":
            print(fila)
            print(fila2)
            break
        else:
            print("Operação inválida! Digite apenas F, G, A, B ou S!")
        x += 1
            
    break
