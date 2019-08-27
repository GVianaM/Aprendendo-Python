# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 33.Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a = int(input("Lado 1:"))
b = int(input("Lado 2:"))
c = int(input("Lado 3:"))
def existe(a, b, c):
    if (b - c) < a < b + c:
        if (a - c) < b < a + c:
            if (a - b) < c < a + b:
                return True
if existe(a, b, c) == True:
    print("Os valores informados podem ser um triângulo")
else:
    print("Os valores informados não formam um triângulo")

if a != b and b != c and a != c and existe(a, b, c) == True:
    print("Esse triângulo é escaleno!")

if a == b and b != c and a != c and existe(a, b, c) == True:
    print("Esse triângulo é isóceles!")
elif a != b and b == c and a != c and existe(a, b, c) == True:
    print("Esse triângulo é isóceles!")
else:
    if a != b and b != c and a == c and existe(a, b, c) == True:
        print("Esse triângulo é isóceles!")

if a == b and b == c and a == c and existe(a, b, c) == True:
    print("Esse triângulo é equilátero!")
print()

# 34.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# A) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
# os demais valores, sendo encerrado;
# B) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# C) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# D) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
a = int(input("Escreva o valor de a:"))
b = int(input("Escreva o valor de b:"))
c = int(input("Escreva o valor de c:"))
if a == 0:
    print("A equação não é do segundo grau!")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Delta é negativo, a equação não possui raizes reais.")
    elif delta == 0:
        print("A equação possui apenas uma raiz real")
        x = (- b + (delta ** (1 / 2))) / 2 * a
        print("Delta:", delta)
        print("X:", round(x, 2))
    else:
        x1 = (- b + (delta ** (1 / 2))) / 2 * a
        x2 = (- b - (delta ** (1 / 2))) / 2 * a
        print("Delta:", delta)
        print("X1:", round(x1, 2))
        print("X2:", round(x2, 2))
print()

# 35. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto
ano = int(input("Escreva o ano para saber se é bissexto:"))
if ano % 400 == 0:
    print("O ano de", ano, "é bissexto")
else:
    if ano % 4 == 0 and ano % 100 != 0:
        print("O ano de", ano, "é bissexto")
    else:
        print("O ano de", ano, "não é bissexto")
print()

# 36. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input("Escreva o dia:"))
mes = int(input("Escreva o mes:"))
ano = int(input("Escreva o ano:"))
mes31 = (1, 3, 5, 7, 8, 10, 12)
mes30 = (4, 6, 9, 11)
mesB6 = 2
valida = False
bissexto = False
if ano % 400 == 0:
    bissexto = True
else:
    if ano % 4 == 0 and ano % 100 != 0:
        bissexto = True
    else:
        bissexto = False
if mes in mes31 and dia >=1 and dia <=31:
    valida = True
elif mes in mes30 and dia >= 1 and dia <=30:
    valida = True
else:
    if bissexto is True and dia >=1 and dia <= 29:
        valida = True
    if bissexto is False and dia >= 1 and dia <= 28:
        valida = True
if valida is True:
    print("Data Válida")
else:
    print("Data Inválida")
print()