"Tabela de Fibonnaci com e sem recursão "

"""
Com recursão:

def fibonacci(n): -> Recursão por cauda:

    if n <= 1:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)

fibonacci(5) -> 9
"""

def fibonacci(n):
    p = 0
    s = 1
    while n > 0:
        p, s = s, s + p
        n -= 1
    print(p)
    return p

fibonacci(4)