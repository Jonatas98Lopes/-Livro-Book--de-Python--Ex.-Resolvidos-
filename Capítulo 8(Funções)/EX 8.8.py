def maior_divisor_comum(a, b): 
    if b == 0:
        return a
    return maior_divisor_comum(b ,a % b) 

def minimo_multiplo_comum(a , b):
    if a == b:
        return 1
    elif b == 1:
        return a
    return abs(a * b) / maior_divisor_comum(a ,b)


a = int(input("Digite o maior número aqui: "))
b = int(input("Digite o menor número aqui: "))
print(minimo_multiplo_comum(a, b))
