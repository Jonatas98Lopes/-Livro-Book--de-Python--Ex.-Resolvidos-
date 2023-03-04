def jogo_da_velha(objeto=" "):
    figura = objeto.upper()
    for x in range(1):
        print(f" {figura} | {figura} |  {figura} ")
        print()
        print("---+---+---")
        print()

jogo_da_velha()