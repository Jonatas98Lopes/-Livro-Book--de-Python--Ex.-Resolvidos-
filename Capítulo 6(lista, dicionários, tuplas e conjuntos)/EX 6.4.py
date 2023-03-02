ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"Digite F para adicionar um cliente ao fim da lista,")
    print("ou A para realizar o atendimento. S para sair")
    operacao = input("Operacao (F, A ou S):")
    if operacao in "Aa":
        atendido = fila.pop(0) # Resulta em erro se a lista estiver vazia.
        print(f"Cliente {atendido} atendido.")
    elif operacao in "Ff":
        ultimo == 1
        fila.append(ultimo)
    elif operacao in "Ss":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
    
