def maior_divisor_comum(a, b): 
    if b == 0:
        return a
    return maior_divisor_comum(b ,a % b) 

a = int(input("Digite o maior número aqui: "))
b = int(input("Digite o menor número aqui: "))
print(maior_divisor_comum(a, b))
