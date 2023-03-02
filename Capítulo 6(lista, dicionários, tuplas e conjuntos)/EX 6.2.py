
# Funcionamento de extend. Este método atribui, apenas, os elementos de outra lsita à mesma.

lista = [2,4,5,6,7,8,9,0,321]
lista_2 = [12,3,4,6,8,9,0,43]
resultado = []
resultado.extend(lista)
resultado.extend(lista_2)
print(resultado)
