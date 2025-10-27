def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de número negativo.")
    return a ** 0.5
