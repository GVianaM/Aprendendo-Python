# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print ("Alo Mundo!")
print()

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input("Escreva um número:")
print("O número informado foi:", numero)
print()

# 3. Faça um Programa que peça dois números e imprima a soma.
print("Vamos somar!!")
a = float(input("Escreva um número:"))
b = float(input("Escreva outro número:"))
soma = a + b
print("O resultado de", a, "+", b, "é:", round(soma, 2))
print()

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("Vamos calcular a média...")
n1 = float(input("Primeira nota:"))
n2 = float(input("Segunda nota:"))
n3 = float(input("Terceira nota:"))
n4 = float(input("Quarta nota:"))
media = (n1 + n2 + n3 + n4) / 4
print("Sua média é:", round(media, 1))
print()

# 5. Faça um Programa que converta metros para centímetros.
print("Converta metros para centímetros")
metro = int(input("Escreva o número de metros:"))
centimetro = metro * 100
if metro == 1:
    print(metro, "metro é igual a", centimetro, "centímetros")
else:
    print(metro, "metros é igual a", centimetro, "centímetros")
print()

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
print("Vamos calcular a área do circulo")
raio = int(input("Informe o valor do raio:"))
areaCirculo = math.pi * raio ** 2
print("A área do circulo é de", round(areaCirculo, 2))
print()

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print("Vamos calcular o dobro da área do quadrado")
lado = int(input("Valor do lado:"))
areaQuadrado = lado * lado
dobroDaArea = 2 * areaQuadrado
print("O dobro da area do quadrado é", dobroDaArea)
print()

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
print("Vamos calcular seu salário!")
ganhoHora = int(input("Quanto voce ganha por hora?"))
horasTrabalhadas = int(input("Quantas horas voce trabalha por mes?"))
salario = ganhoHora * horasTrabalhadas
print("Seu salário por mes é de R$", float(salario))