ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"Digite F para adicionar um cliente ao fim da lista,")
    print("ou A para realizar o atendimento. S para sair")
    operacao = input("Operacao (F, A ou S):")
    x = 0
    while x < len(operacao):
        if operacao[x] in "Aa":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] in "Ff":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] in "Ss":
            print(fila)
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1
            
    break
