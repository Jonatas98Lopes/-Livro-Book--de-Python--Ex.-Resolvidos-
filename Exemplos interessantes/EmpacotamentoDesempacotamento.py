'''
 Empacotamento: Quando usamos o asterisco em uma lista passada como argumento na chamada de uma função.
 Neste caso, estamos dizendo que todos os elementos daquela lista serão divididos para todos os parâmetros.

 Exemplo:
def soma_tres_numeros(a, b, c):
    return (a + b + c)
L =[2, 6, 9]
soma_tres_numeros(*L)
'''

def soma_tres_numeros(a, b, c):
    return (a + b + c)
L =[2, 6, 9]
print(soma_tres_numeros(*L))

"""
 Desempacotamento: Quando usamos o asterisco num dos parâmetros de uma função.
 Neste caso, estamos dizendo que a função receberá um número indeterminado de argumentos.
 Considerados como listas de parâmetros, você pode não os passar, como incluir infinitos.

 Exemplo:

 def imprime_maior(mensagem,*numeros): -> Para evitar problemas, sempre passe o parâmetro obrigatório primeiro.
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)

imprime_maior("Maior: ",1,2,3,4,5)

"""

def imprime_maior(mensagem,*numeros): 
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)

imprime_maior("Maior: ",1,2,3,4,5)

"""
 Funções lambda: Funções lambda executam um papel importante. São funções sem nome, e encurtadas.
 Eles são usadas quando a função é pequena ou pouco usada, com o objetivo de encurtar o código.

 a = lambda x: x * 3
 print(a(23))
"""

a = lambda x: x * 3
print(a(23))