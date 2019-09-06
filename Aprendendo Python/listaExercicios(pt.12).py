# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 52. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.
num = 1
while num <= 20:
    print(num)
    num += 1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in nums:
    print(i, end=' ')
print()

# 53. Faça um programa que leia 5 números e informe o maior número.
for i in range(5):
    numeros = float(input("Escreva um número:"))
    if 'maior' in vars():
        if numeros > maior:
            maior = numeros
    else:
        maior = numeros
print("O maior número escrito foi:", maior)
print()

# 54. Faça um programa que leia 5 números e informe a soma e a média dos números.
lista = []
for i in range(5):
    numero = float(input("Escreva um número:"))
    lista.append(numero)
print("O resultado da soma dos números é:", round(sum(lista), 2))
print("A média dos números é de:", round(sum(lista) / 5, 2))
print()

# 55. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
print("Ímpares entre 1 e 50")
impar = 1
while impar <= 50:
    if impar % 2 == 0:
        impar += 1
    else:
        print("Os números ímpares são:", impar)
        impar += 1
print()

# 56. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
number1 = int(input("Escreva um número inteiro:"))
number2 = int(input("Escreva outro número inteiro:"))
print("Os números entre", number1, "e", number2, "são:")
for x in range(number1 + 1, number2):
    print(x)
for y in range(number2 - 1, number1):
    print(y)
print()

# 57. Altere o programa anterior para mostrar no final a soma dos números.
number1 = int(input("Escreva um número inteiro:"))
number2 = int(input("Escreva outro número inteiro:"))
print("Os números entre", number1, "e", number2, "são:")
for x in range(number1 + 1, number2):
    print(x)
for y in range(number2 - 1, number1):
    print(y)
soma = number1 + number2
print("O resultado da soma dos números informados é:", soma)
print()