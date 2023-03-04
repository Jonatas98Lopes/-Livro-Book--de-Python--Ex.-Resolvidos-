# Verificação de opções de ações em string.

def verifica_opcoes(opcoes):
    suplementar = []
    for i in opcoes:
        suplementar.append(i.lower())
    while True:
        escolha = input(f"Digite a opção que seja executar: {suplementar}: ").lower().strip()
        if escolha in suplementar:
            print("Executando operação...\nPor favor aguarde mais um pouco")
            return
        print("Operação inválida. Por favor, digite uma das opções válidas.")    

acoes = 'SADF'
verifica_opcoes(acoes)
