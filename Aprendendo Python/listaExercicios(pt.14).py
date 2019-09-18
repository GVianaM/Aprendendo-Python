# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 63. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
fatorial = int(input("Informe o número fatorial:"))
resultado = 1
for i in range(1, fatorial + 1):
    resultado *= i
print("Fatorial de", fatorial, 'é igual a:', resultado)
print()

# 64. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
tamanho = int(input("Quantos números você deseja inserir?"))
lista = []
maior = 0
if tamanho < 0:
    print("O tanto de número à ser inserido precisa ser positivo!")
    exit()
while tamanho > 0:
    num = int(input("Digite um número:"))
    tamanho -= 1
    lista.append(num)
    for i in lista:
        if num > maior:
            maior = num
        if 'menor' not in vars() or num < menor:
            menor = num
print("O maior número é:", maior)
print("O menor número é:", menor)
print("A soma dos números da um total de:", sum(lista))
print()

# 65. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
tamanho = int(input("Quantos números você deseja inserir?"))
lista = []
maior = 0
if tamanho < 0:
    print("O tanto de número à ser inserido precisa ser positivo!")
    exit()
while tamanho > 0:
    num = int(input("Digite um número:"))
    tamanho -= 1
    lista.append(num)
    if num < 0 or num > 1000:
        print("Os números precisam estar entre 0 e 1000!")
        exit()
    for i in lista:
        if num > maior:
            maior = num
        if 'menor' not in vars() or num < menor:
            menor = num
print("O maior número é:", maior)
print("O menor número é:", menor)
print("A soma dos números da um total de:", sum(lista))
print()

# 66.Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
# limitando o fatorial a números inteiros positivos e menores que 16.
vezes = int(input("Quantos cálculos fatorias você deseja fazer?"))
while vezes > 0:
    fatorial = int(input("Informe o número fatorial:"))
    if fatorial < 0 or fatorial > 16:
        print("O fatorial precisa estar abaixo de 16 e acima de 0!")
        exit()
    vezes -= 1
    resultado = 1
    for i in range(1, fatorial + 1):
        resultado *= i
    print("Fatorial de", fatorial, 'é igual a:', resultado)
print()

# 67. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input("Escreva um número:"))
if num == 2 or (num != 1 and num % 2 == 1):
    print(num, "é primo!")
else:
    print(num, "não é primo!")
print()

# 68. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
num = int(input("Escreva um número:"))
if num == 2 or (num != 1 and num % 2 == 1):
    print(num, "é primo!")
else:
    print(num, "não é primo!")
    divisiveis = []
    for i in range(1, 101):
        if num % i == 0:
            result = num / i
            divisiveis.append(result)
    print("O número", num, "é divisível por:", divisiveis)
print()