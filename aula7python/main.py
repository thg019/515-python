# 01) FAÇA UMA FUNÇÃO QUE RECEBA DOIS NÚMEROS E RETORNE A SOMA
# DESSES DOIS NÚMEROS

# def somar(num1, num2):
#     return num1 + num2

# numero1 = float(input("Digite aqui o primeiro numero: "))
# numero2 = float(input("Digite aqui o segundo numero: "))

# print(somar(numero1, numero2))


# 02) FAÇA UMA FUNÇÃO LAMBDA QUE RECEBA UM NÚMERO E RETONE ELE ELEVADO AO QUADRADO

# elevado = lambda numero : numero**2
# numero = float(input("Digite um numero: "))

# print(elevado(numero))

# 03) FAÇA UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS E RETORNE QUAL É O MAIOR ENTRE ELES

# def numero_maior(lista):
#     return max(lista)

# lista = []
# for i in range(5):
#     numero = float(input("Digite aqui um numero: "))
#     lista.append(numero)
    
# print(numero_maior(lista))
    
# 04) FAÇA UMA FUNÇÃO LAMBDA PARA MULTIPLICAR TODOS OS NÚMEROS DE UMA LISTA POR 2


# lista = []

# for i in range (5):
#     numero = float(input("Digite aqui um numero: "))
#     lista.append(numero)

# lista_multiplicada = list(map(lambda numero : numero*2, lista))
# print(lista_multiplicada)

# 05) FAÇA UMA FUNÇÃO LAMBDA QUE RECEBE UM NÚMERO E VERIFICA SE O NÚMERO É PAR

# par_ou_impar = lambda numero : "par" if numero % 2 == 0 else "ímpar"
# numero = int(input("Digite um número: "))
# print(par_ou_impar(numero))

# 06) FAÇA UMA FUNÇÃO QUE RECEBA UMA LISTA DE NÚMERO E RETORNE A MÉDIA DOS NÚMEROS DESSA LISTA
# def media (lista): 
#     return sum(lista) / len(lista)  # metodo mais clean

# #metodo mais manual
# def media (lista):
#     soma = 0
#     for numero in lista:
#         soma = soma + numero
#     media = soma / len(lista)
#     return media

# quantidade = int(input("Digite a quantidade de números que você vai inserir na lista: "))

# lista = []
# for i in range(quantidade):
#     numero = float(input("Digite um número: "))
#     lista.append(numero)

# print(media(lista))

# 07) FAÇA UMA FUNÇÃO QUE RECEBE UM TEXTO E RETORNE A QUANTIDADE DE VOGAIS QUE AQUELE TEXTO CONTÉM

def contar_vogais(texto):
    if letra in 'aeiouAEIOU'

# 08) FAÇA UMA FUNÇÃO QUE RECEBA UM TEXTO E RETORNA Q QUANTIDADE DE CONSOANTES QUE AQUELE TEXTO CONTÉM

# 09) FAÇA UMA FUNÇÃO QUE RECEBE UM NÚMERO E RETORNA O SEU VALOR FATORIAL

# 10) FAÇA UMA FUNÇÃO QUE RECEBE UMA SENHA E INFORMA SE ELA É UMA SENHA FORTE
