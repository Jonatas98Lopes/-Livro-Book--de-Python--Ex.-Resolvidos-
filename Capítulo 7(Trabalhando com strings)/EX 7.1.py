string_1 = "AABBEFAATT"
string_2 = "BE"
resultado = string_1.find(string_2)
if resultado >= 0:
    print(f"{string_2} encontrado na posição {resultado} de {string_1}.")
else:
    print(f"Nenhum {string_2} encontrado em {string_1}. ")
