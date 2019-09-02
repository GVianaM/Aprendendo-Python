# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 42.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
num1 = input("Escreva um número:")
num2 = input("Escreva outro número:")
print("Digite + para Somar, - para Subtrair, / para Dividir, X para Multiplicar e P para potencializar.")
operacao = input("Escreva a operação que deseja fazer:")
try:
    a = int(num1)
    try:
        b = int(num2)
        if operacao == '+':
            resultado = a + b
        elif operacao == '-':
            resultado = a - b
        elif operacao == '/':
            resultado = a / b
        elif operacao == 'X' or operacao == 'x':
            resultado = a * b
        elif operacao == 'P' or operacao == 'p':
            resultado = a ** b
        else:
            print('Escreva o símbolo de operação correto!')
            exit()
    except:
        try:
            b = float(num2)
            if operacao == '+':
                resultado = a + b
            elif operacao == '-':
                resultado = a - b
            elif operacao == '/':
                resultado = a / b
            elif operacao == 'X' or operacao == 'x':
                resultado = a * b
            elif operacao == 'P' or operacao == 'p':
                resultado = a ** b
            else:
                print('Escreva o símbolo de operação correto!')
                exit()
        except:
            print('Precisamos utilizar apenas números!!')
except:
    try:
        a = float(num1)
        try:
            b = int(num2)
            if operacao == '+':
                resultado = a + b
            elif operacao == '-':
                resultado = a - b
            elif operacao == '/':
                resultado = a / b
            elif operacao == 'X' or operacao == 'x':
                resultado = a * b
            elif operacao == 'P' or operacao == 'p':
                resultado = a ** b
            else:
                print('Escreva o símbolo de operação correto!')
                exit()
        except:
            try:
                b = float(num2)
                if operacao == '+':
                    resultado = a + b
                elif operacao == '-':
                    resultado = a - b
                elif operacao == '/':
                    resultado = a / b
                elif operacao == 'X' or operacao == 'x':
                    resultado = a * b
                elif operacao == 'P' or operacao == 'p':
                    resultado = a ** b
                else:
                    print('Escreva o símbolo de operação correto!')
                    exit()
            except:
                print('Precisamos utilizar apenas números!!')
    except:
        print('Precisamos utilizar apenas números!!')
print("O resultado é:", resultado)
if resultado % 2 == 0:
    print("Esse número é par!")
else:
    print("Esse número é ímpar!")
if resultado >= 0:
    print("O número é positivo")
else:
    print("O número é negativo")
if type(resultado) == type(1):
    print("O número é inteiro")
else:
    if type(resultado) == type(0.1):
        print("O número é decimal")
print()

# 43. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".
print("Responda as perguntas com 'S' de sim ou 'N' de não ")
perg1 = input("Telefonou para vítima?")
perg2 = input("Esteve no local do crime?")
perg3 = input("Mora perto da vítima?")
perg4 = input("Devia para a vítima?")
perg5 = input("Já trabalhou com a vítima?")
pontos = 0
perguntas = [perg1, perg2, perg3, perg4, perg5]
if len(perg1) > 1 or len(perg2) > 1 or len(perg3) > 1 or len(perg4) > 1 or len(perg5) > 1:
    print("Responda apenas com 1 'S' ou 1 'N' por pergunta!")
    exit()
for letra in perguntas:
    if letra == 's' or letra == 'S':
        pontos += 1
if pontos == 2:
    print("Suspeita!")
elif pontos == 3 or pontos == 4:
    print("Cúmplice!")
elif pontos == 5:
    print("Assasino!")
else:
    print("Inocente!")
print()