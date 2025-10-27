def ler_numero(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def exibir_menu():
    print("\n=== Calculadora CLI ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("0. Sair")
