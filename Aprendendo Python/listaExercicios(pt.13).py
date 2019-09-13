# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 58. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("Escreva um número:"))
for i in lista:
    if num < 1 or num > 10:
        print("O número precisa estar entre 1 e 10!")
        break
    result = num * i
    print(num, "X", i, "=", result)
print()

# 59. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.
base = int(input("Informe a base:"))
expoente = int(input("Informe o expoente:"))
while expoente <= 0 :
    expoente = int(input("Informe o expoente:"))
    if expoente <= 0:
        print("O expoente precisa ser positivo!")
resultado = 1
for i in range(1, expoente + 1):
    resultado *= base
print(base, "elevado a", expoente, "é igual a:", resultado)
print()

# 60. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
# números impares.
list = []
par = 0
impar = 0
while len(list) < 10:
    number = int(input("Escreva um número:"))
    list.append(number)
for i in list:
    if i % 2 == 0:
        par +=1
    else:
        impar += 1
print("Quantidade de números")
print("Pares:", par)
print("Ímpares:", impar)
print()

# 61. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo
n = int(input("Informe o termo desejável para Fibonacci:"))
def fib(n):
    a = 0
    b = 1
    print(a)
    while b < n:
        c = a
        a = b
        b = a + c
        print(a, end=' ')
fib(n)
print()

# 62. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500
def fib(n):
    a = 0
    b = 1
    print(a)
    while b < n:
        c = a
        a = b
        b = a + c
        print(a, end=' ')
fib(700)
print()