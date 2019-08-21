# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
peso = float(input("Escreva o peso dos peixes:"))
if peso >= 51:
    excesso = peso - 50
    multa = excesso * 4
    print("O peso dos peixes excederam em", excesso, "Kg e o valor da multa será de", multa, "reais.")
else:
    print('O peso dos peixes é de', peso, "Kg")
print()

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
# 11% para o Imposto de Renda,
# 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
ganho = float(input("Quanto voce ganha por hora?"))
horas = int(input("Quantas horas voce trabalha no mes?"))
salBruto = ganho * horas
ir = 11 * salBruto / 100
inss = 8 * salBruto / 100
sind = 5 * salBruto / 100
desctotal = ir + inss + sind
salLiquido = salBruto - desctotal
print("Salário Bruto: R$", salBruto)
print("Imposto de Renda: R$", ir)
print("INSS: R$", inss)
print("Sindicato: R$", sind)
print("Salário Líquido: R$", salLiquido)

# 16. Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math
area = float(input("Qual tamanho da área, em m2, a ser pintada?"))
qtdLata = area / 54
precoTotal = math.ceil(qtdLata) * 80
print("Para pintar uma área de", area, "m2 será preciso", math.ceil(qtdLata), "lata(s)")
print("O valor total das latas é de: R$", round(precoTotal, 2))
print()

# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
# isto é, considere latas cheias.
import math
area = float(input("Qual tamanho da área, em m2, a ser pintada?"))
qtdLata = area / 108
qtdGalao = area / 21.6
precoLata = math.ceil(qtdLata) * 80
precoGalao = math.ceil(qtdGalao) * 25
print("Para pintar uma área de", area, "m2 apenas com latas será necessário", math.ceil(qtdLata), "lata(s) que custarão", precoLata, "reais")
print("Para pintar uma área de", area, "m2 apenas com galões será necessário", math.ceil(qtdGalao), "galão(ões) que custarão", precoGalao, "reais")
litros = (area / 6) * 1.1 # 10%
mLatas = litros / 18
mGalao = (litros - round(mLatas) * 18) / 3.6
precoTotal = round(mLatas) * 80 + round(mGalao) * 25
print("Para pintar uma área de", area, "m2 com latas e galões será necessário", round(mLatas), "lata(s) e", round(mGalao), "galões que custarão", precoTotal,"reais")
print()

# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = float(input("Qual tamanho do arquivo a ser baixado em MB?"))
velocidade = int(input("Qual a velocidade da sua internet?"))
mbps = velocidade / 8
segundos = tamanho / mbps
tempo = segundos / 60
print("O download de", tamanho, "MB irá demorar", round(tempo, 2), "minutos")