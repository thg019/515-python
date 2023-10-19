from operacoes import *

numero1 = int(input("Digite aqui o primeiro numero: "))
numero2 = int(input("Digite aqui o segundo numero: "))

while True:
    calculadora = int(input("""
            1 - Somar
            2 - Subtrair
            3 - Multiplicar
            4 - Dividir
            0 - Sair
    """))
    
    if calculadora == 1:
        print(somar(numero1, numero2))
    elif calculadora == 2:
        print(subtrair(numero1, numero2))
    elif calculadora == 3:
        print(multiplicar(numero1, numero2))
    elif calculadora == 4:
        print(dividir(numero1, numero2))
    elif calculadora == 0:
        break
    else:
        print("Opção inválida.")