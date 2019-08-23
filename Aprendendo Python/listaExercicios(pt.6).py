# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 29. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Escreva o seu salário:"))
if salario <= 280.0:
    salarioAtual = salario * 0.2 + salario
    print("Antes do reajuste: R$", salario)
    print("O percentual de aumento foi de 20%")
    print("O valor do aumento foi de R$", round((salarioAtual - salario), 2))
    print("O salario atual é de R$",salarioAtual)
elif salario >= 281.0 and salario < 700.0:
    salarioAtual = salario * 0.15 + salario
    print("Antes do reajuste: R$", salario)
    print("O percentual de aumento foi de 15%")
    print("O valor do aumento foi de R$", round((salarioAtual - salario), 2))
    print("O salario atual é de R$", salarioAtual)
elif salario >= 700.0 and salario < 1500.0:
    salarioAtual = salario * 0.1 + salario
    print("Antes do reajuste: R$", salario)
    print("O percentual de aumento foi de 10%")
    print("O valor do aumento foi de R$", round((salarioAtual - salario), 2))
    print("O salario atual é de R$", salarioAtual)
else:
    salarioAtual = salario * 0.05 + salario
    print("Antes do reajuste: R$", salario)
    print("O percentual de aumento foi de 5%")
    print("O valor do aumento foi de R$", round((salarioAtual - salario), 2))
    print("O salario atual é de R$", salarioAtual)
print()

# 30. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#Salário Bruto: (5 * 220): R$ 1100, 00
#IR(5 %): R$ 55, 00
#INSS (10 %): R$ 110, 00
#FGTS(11 %): R$ 121, 00
#Total de descontos: R$ 165, 00
#Salário Liquido: R$ 935, 00
hora = float(input("Quantas horas voce trabalha por mes?"))
valor = float(input("Quanto ganha por hora?"))
salBruto = hora * valor
if salBruto <= 900.00:
    ir = 0
    porcentagem = "Isento"
elif salBruto >= 901.00 and salBruto <= 1500.00:
    ir = salBruto * 0.05
    porcentagem = 5
elif salBruto >= 1501.00 and salBruto <= 2500.00:
    ir = salBruto * 0.1
    porcentagem = 10
else:
    ir = salBruto * 0.2
    porcentagem = 20
inss = salBruto * 0.1
fgts = salBruto * 0.11
descontos = ir + inss
salLiquido = salBruto - descontos
print("Salário Bruto: R$", salBruto)
print("IR (", porcentagem,"% ): R$", round(ir, 2))
print("INSS (10%): R$", round(inss, 2))
print("FGTS (11%): R$", round(fgts, 2))
print("Total de descontos: R$", round(descontos, 2))
print("Salário Líquido: R$", salLiquido)
print()

# 31. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.
dia = int(input("Escreva um número:"))
if dia == 1:
    print("1 - Domingo")
elif dia == 2:
    print("2 - Segunda")
elif dia == 3:
    print("3 - Terça")
elif dia == 4:
    print("4 - Quarta")
elif dia == 5:
    print("5 - Quinta")
elif dia == 6:
    print("6 - Sexta")
elif dia == 7:
    print("7 - Sábado")
else:
    print("Valor Inválido!")
print()

# 32. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento            Conceito
# Entre 9.0 e 10.0                      A
# Entre 7.5 e 9.0                       B
# Entre 6.0 e 7.5                       C
# Entre 4.0 e 6.0                       D
# Entre 4.0 e zero                      E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input("Escreva sua nota:"))
nota2 = float(input("Escreva a outra nota:"))
media = (nota1 + nota2) / 2
if media >= 9.0 and media <= 10.0:
    conceito = str("A")
elif media >= 7.5 and media <= 8.9:
    conceito = str("B")
elif media >= 6.0 and media <= 7.4:
    conceito = str("C")
elif media >= 4.0 and media <= 5.9:
    conceito = str("D")
else:
    conceito = str("E")
if conceito == str("A") or conceito == str("B") or conceito == str("C"):
    print("APROVADO!")
else:
    print("REPROVADO!")
print("Notas: 1:", nota1, '\n', "2:", nota2)
print("Média:", media)
print("Conceito:", conceito)
print()