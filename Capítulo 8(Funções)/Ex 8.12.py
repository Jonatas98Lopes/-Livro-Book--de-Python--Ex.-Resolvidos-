def compara_string_lista(texto, lista): # -> Simplifique o bloco de instruções -> return texto in lista
    if texto in lista:
        return True
    return False

a = "carro"
l = ["casa","castelo","carro","rato","ovo","mistério"]
print(compara_string_lista(a, l))
