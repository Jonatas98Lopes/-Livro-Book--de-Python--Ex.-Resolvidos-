estoque = {
    "Tomate": [1000, 2.30],
    "Alface": [500, 0.45],
    "Batata": [2001, 1.20],
    "Feijão": [100, 1.50]
}


vendas = []
while True:
    produto = input("Digite o nome do produto. (fim) para sair: ")
    if produto == "fim":
        break
    while produto not in estoque:
        print("Não possuímos este produto em estoque. Por favor, digite outro produto.\n")
        produto = input("Digite o nome do produto. (fim) para sair: ")
        if produto == "fim":
            break
    quantidade = int(input("Qual a quantidade vendida? "))
    while quantidade > estoque[produto][0]:
        print("Quantidade vendida acima do limite em estoque. Por favor, digite novamente.\n")
        quantidade = int(input("Qual a quantidade vendida? "))
    vendas.append([produto, quantidade])
total = 0
for operacao in vendas:
    nome_produto, quantidade = operacao
    preco = estoque[nome_produto][1]
    custo = quantidade * preco
    print(f"{nome_produto} -> {quantidade} solicitado -> Preço unitário: R$ {preco:.2f} -> Valor recebido: R$ {custo:.2f}\n")
    estoque[nome_produto][0] -= quantidade
    total += custo
print(f"Valor total vendido: R$ {total:.2f}\n")
print("Estoque:\n")
for chave, valor in estoque.items():
    print(f"Descrição: {chave}")
    print(f"Quantidade: {valor[0]}")
    print(f"Valor unitário: R$ {valor[1]:.2f}")