# Função validação de entrada para o número mínimo e máximo de caracteres:
# Devemos retorna verdadeiro caso a quantidade de caracteres esteja dentro do intervalo determinado.
# Falso caso contrário.
def verifica_string(texto, qtd_min, qtd_max):
    if len(texto) >=  qtd_min and len(texto) <= qtd_max:
        return True
    return False

caracteres = input("Digite uma frase: ")
print(verifica_string(caracteres, 5, 20))