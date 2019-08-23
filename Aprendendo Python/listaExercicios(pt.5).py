# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 25. Faça um Programa que leia três números e mostre o maior e o menor deles.
x = float(input("Escreva um número:"))
y = float(input("Escreva outro número:"))
z = float(input("Escreva mais um número:"))
def maior(x, y, z):
    if x >= y and x >= z:
        print(x, "é o maior número")
    elif y >= x and y >= z:
        print(y, "é o maior número")
    else:
        print(z, "é o maior número")
def menor(x, y, z):
    if x <= y and x <= z:
        print(x, "é o menor número")
    elif y <= x and y <= z:
        print(y, "é o menor número")
    else:
        print(z, "é o menor número")
maior(x, y, z)
menor(x, y, z)
print()

# 26. Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
prod1 = float(input("Escreva o preço do primeiro produto:"))
prod2 = float(input("Escreva o preço do segundo produto:"))
prod3 = float(input("Escreva o preço do terceiro produto:"))
if prod1 < prod2 and prod1 < prod3:
    print("Leve o produto que custa R$", prod1)
elif prod2 < prod1 and prod2 < prod3:
    print("Leve o produto que custa R$", prod2)
elif prod3 < prod1 and prod3 < prod2:
    print("Leve o produto que custa R$", prod3)
else:
    print("Escolha um dos produtos que possui o mesmo valor para levar.")
print()

# 27. Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input("Escreva um número:"))
num2 = float(input("Escreva mais um número:"))
num3 = float(input("Escreva outro número:"))
if num1 >= num2 and num1 >= num3:
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 >= num1 and num2 >= num3:
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
print()

# 28. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Digite 'M' para Matutino, 'V' para Vespertino ou 'N' para Noturno")
turno = str(input("Em qual turno você estuda?"))
if turno == "M" or turno == "m":
    print("Bom Dia!")
elif turno == "V" or turno == "v":
    print("Boa Tarde!")
elif turno == "N" or turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
print()