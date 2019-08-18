# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
print("Vamos converter Farenheit para Celsius")
f = float(input("Quantos graus Farenheit?"))
c = (f - 32) / 1.8
print(f, "graus Farenheit são", c, "graus Celsius")
print()

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
print("Vamos converter Celsius para Farenheit")
c = float(input("Quantos graus Celsius?"))
f = 1.8 * c + 32
print(c, "graus Celsius são", f, "graus Farenheit")
print()

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo .
# B) a soma do triplo do primeiro com o terceiro.
# C) o terceiro elevado ao cubo.
a = int(input("Escreva um número inteiro:"))
b = int(input("Escreva mais um inteiro:"))
c = float(input("Escreva um número real:"))
A = a * 2 + b / 2
B = a * 3 + c
C = c ** 3
print('',"A)", A,'\n', "B)", B, '\n', "C)", C)
print()

# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
# usando a seguinte fórmula: (72.7*altura) - 58
print("Vamos calcular o peso ideal!")
altura = float(input("Escreva sua altura:"))
pesoIdeal = 72.7 * altura - 58
print("Seu peso ideal é de", round(pesoIdeal, 2), "Kg.")
print()

# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
print("Descubra seu peso ideal")
h = float(input("Escreva sua altura:"))
pesoHomens = 72.7 * h - 58
pesoMulheres = 62.1 * h - 44.7
print("O peso ideal para homens de", h, "m é de", round(pesoHomens, 2), "Kg")
print("O peso ideal para mulheres de", h, "m é de", round(pesoMulheres, 2), "Kg")
print()
