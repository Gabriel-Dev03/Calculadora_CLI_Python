# main.py

from calculos import somar, subtrair, multiplicar, dividir, potencia, raiz_quadrada
from utils import ler_numero, exibir_menu

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo da calculadora. Até logo!")
            break
        elif opcao in ["1", "2", "3", "4", "5"]:
            a = ler_numero("Digite o primeiro número: ")
            b = ler_numero("Digite o segundo número: ")

            try:
                if opcao == "1":
                    print(f"Resultado: {somar(a, b)}")
                elif opcao == "2":
                    print(f"Resultado: {subtrair(a, b)}")
                elif opcao == "3":
                    print(f"Resultado: {multiplicar(a, b)}")
                elif opcao == "4":
                    print(f"Resultado: {dividir(a, b)}")
                elif opcao == "5":
                    print(f"Resultado: {potencia(a, b)}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "6":
            a = ler_numero("Digite o número: ")
            try:
                print(f"Resultado: {raiz_quadrada(a)}")
            except ValueError as e:
                print(f"Erro: {e}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
