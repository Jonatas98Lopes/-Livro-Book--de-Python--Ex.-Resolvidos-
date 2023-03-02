while True:
    qtd_palavras = int(input("Em quantas palavras quer desafiar seu adversário? "))
    if qtd_palavras >= 1 and qtd_palavras <= 10:
        break
    print("Número inválido! Digite um número entre 1 e 10.\n")

palavras = []
for i in range(qtd_palavras):
    palavra = input("Digite a palavra secreta: ").lower().strip()
    palavras.append(palavra)
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while len(palavras) > 0:
    numero = int(input("Qual a palavra secreta que deseja responder? "))
    indice = (numero * 776) % len(palavras)
    palavra_secreta = palavras[indice - 1]
    while True:
        senha = ""
        for letra in palavra_secreta:
            senha += letra if letra in acertos else "."
        print(senha)
        if senha == palavra_secreta:
            print(f"Você acertou a palavra {numero}!")
            deletar = palavras.index(palavra_secreta)
            del palavras[deletar]
            acertos.clear()
            digitadas.clear()
            erros = 0
            break
        tentativa = input("\nDigite uma letra: ").lower().strip()
        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra_secreta:
                acertos += tentativa
            else:
                erros += 1
                print("Você errou!")
            print("X==:==\nX  :  ")
            print("X  O  " if erros >= 1 else "X")
            linha2 = ""
            if erros == 2:
                linha2 =  "  |  "
            elif erros == 3:
                linha2 =  " \|  "
            elif erros >= 4:
                linha2 =  " \|/ "
            print(f"X{linha2}")
            linha3 = ""
            if erros == 5:
                linha3 +=  " /  "
            elif erros >= 6:
                linha3 +=  " / \ "
            print(f"X{linha3}")
            print(f"X\n===========")
            if erros == 6:
                break
    if erros == 6:
        print("Enforcado! Você perdeu!\n")
        print(f"A palavra secreta era {palavra_secreta}")
        break
else:
    print("Parabéns! Você respondeu todas as palavras corretamente.") 
                
    