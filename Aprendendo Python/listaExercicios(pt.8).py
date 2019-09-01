# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 37. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
num = int(input("Escreva um número até 999:"))
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10
if num > 999:
    print("Apenas números até 999!")
if num <= 999:
    print(num, "=", centena, "centena(s),", dezena, "dezena(s) e", unidade, "unidade(s)")
print()

# 38. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
n1 = float(input("Escreva a Nota 1:"))
n2 = float(input("Escreva a Nota 2:"))
n3 = float(input("Escreva a Nota 3:"))
media = (n1 + n2 + n3) / 3
if media < 0:
    print("As notas devem ser números positivos!")
if media == 10:
    print("Aprovado com Distinção!")
if round(media, 1) >= 7 and round(media, 1) < 10:
    print("Aprovado! Sua média foi:", round(media, 1))
if round(media, 1) < 7 and media >= 0:
    print("Reprovado! Sua média foi:", round(media, 1))
print()

# 39. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
# depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
saque = int(input("Informe o valor do saque:"))
saq = saque
nota100 = saque // 100 % 10
nota50 = 0
nota10 = 0
nota5 = 0
nota1 = 0
if saque < 10 or saque > 600:
    print("O valor do saque é de no mínimo R$10,00 e no máximo R$600,00")
    exit()
while saque >= 100:
    nota100 = saque // 100 % 10
    saque -= nota100 * 100
while 50 <= saque < 100:
    nota50 += 1
    saque -= 50
while 10 <= saque < 50:
    nota10 += 1
    saque -= 10
while 5 <= saque < 10:
    nota5 += 1
    saque -= 5
while 1 <= saque < 5:
    nota1 += 1
    saque -= 1

print("Para R$", saq)
print("Notas de 100:", nota100)
print("Notas de 50:", nota50)
print("Notas de 10:", nota10)
print("Notas de 5:", nota5)
print("Notas de 1:", nota1)
print()

# 40. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
numero = int(input("Escreva um número inteiro:"))
if numero % 2 == 0:
    print("O número", numero, "é par!")
else:
    print("O número", numero, "é ímpar!")
print()

# 41. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
num = input("Escreva um número:")
try:
    a = int(num)
    print("O número", num, "é inteiro!")
except:
    try:
        b = float(num)
        print("O número", num, "é decimal!")
    except:
        print("O valor precisa ser um número")
print()