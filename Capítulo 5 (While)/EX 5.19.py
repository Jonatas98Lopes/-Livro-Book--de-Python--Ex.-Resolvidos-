

valor = float(input("Qual valor deseja sacar? "))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual < apagar:
        apagar -= atual
        cedulas += 1
    elif atual == round(apagar, 2):
        apagar = 0
        cedulas += 1
    else:
        print(f"{cedulas} cédula(a) de R$ {atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.10:
            atual = 0.05
        else:
            atual = 0.01
        cedulas = 0
