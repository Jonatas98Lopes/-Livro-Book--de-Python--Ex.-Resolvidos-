pilha = []
leitor = input("Digite o conjunto de parênteses: ")
x = 0
adiciona = 1
while x < len(leitor):
    if leitor[x] == '(':
        pilha.append(adiciona)
        adiciona += 1
    elif leitor[x] == ')' and len(pilha) > 0:
        pilha.pop(-1)
    else:
        print("Erro")
        break
    x += 1
else:
    if len(pilha) == 0:
        print("OK")
    else:
        print("Erro")
