from random import randint

def  gera_lista(qtd_elementos, vmin=1, vmax=100):
    L = []
    for i in range(qtd_elementos):
        L.append(randint(vmin, vmax))
    return L


versao_inicial = set(gera_lista(20))
versao_final = set(gera_lista(20))

print(versao_inicial)                            
print(versao_final)                            

print()
print(versao_inicial & versao_final)                            #Elementos que não mudaram.
print(versao_final - versao_inicial)                            #Os novos elementos.
print(versao_inicial - versao_final)                            #Os elementos que foram removidos.