# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 44. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro. Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo
# cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
print("Digite 'G' para Gasolina e 'A' para álcool")
combustivel = input("Qual tipo irá colocar?")
litros = float(input("Quantos litros irá colocar?"))
if combustivel == 'A' or combustivel == 'a':
    if litros <= 20:
        desconto = (3 * 1.90) / 100
        precoAlcool = (litros * 1.90) - (desconto * litros)
    if litros > 20:
        desconto = (5 * 1.90) / 100
        precoAlcool = (litros * 1.90) - (desconto * litros)
    print("O valor a ser pago será de R$", round(precoAlcool, 2))
elif combustivel == 'G' or combustivel == 'g':
    if litros <= 20:
        desconto = (4 * 2.50) / 100
        precoGasolina = (litros * 2.5) - (desconto * litros)
    if litros > 20:
        desconto = (6 * 2.50) / 100
        precoGasolina = (litros * 2.5) - (desconto * litros)
    print("O valor a ser pago será de R$", round(precoGasolina, 2))
else:
    print("Utilize as letras corretas para o tipo de combustível")
    exit()
print()

# 45.Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
# a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
morango = float(input("Quantos Kg de morango comprará?"))
maca = float(input("Quantos Kg de maçã comprará?"))
kilosTotais = morango + maca
if morango <= 5:
    precoMorango = morango * 2.50
if morango > 5:
    precoMorango = morango * 2.20
if maca <= 5:
    precoMaca = maca * 1.80
if maca > 5:
    precoMaca = maca * 1.50
precoTotal = precoMaca + precoMorango
if kilosTotais > 8 or precoTotal > 25.0:
    desconto = precoTotal * 10 / 100
    precoAtual = precoTotal - desconto
    print("O valor total da compra é de R$", round(precoAtual, 2))
else:
    print("O valor total da compra é de R$", round(precoTotal, 2))
print()

# 46. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
# ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
# pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
# valor do desconto e valor a pagar.
print("Digite 'F' para File Duplo, 'A' para Alcatra ou 'P' para Picanha")
tipoCarne = input("Qual tipo de carne irá levar?")
kilos = float(input("Quantos Kg irá levar?"))
print("Para forma de pagamento digite 'C' para Cartão Tabajara ou 'D' para Dinheiro")
pagamento = input("Qual a forma de pagamento?")
if tipoCarne == 'F' or tipoCarne == 'f':
    if kilos <= 5:
        preco = kilos * 4.90
    if kilos > 5:
        preco = kilos * 5.80
    if pagamento == 'C' or pagamento == 'c':
        desconto = (preco * 5) / 100
        precoAtual = preco - desconto
    elif pagamento == 'D' or pagamento == 'd':
        desconto = 0
        precoAtual = preco
    else:
        print("Digite a forma de pagamento correta!")
        exit()
    print("Tipo de carne: File Duplo")
    print("Quantidade:", round(kilos, 2))
    print("Preço Total:", round(preco, 2))
    print("Tipo de pagamento:", pagamento)
    print("Desconto:", round(desconto, 2))
    print("Valor a pagar:", round(precoAtual, 2))
elif tipoCarne == 'A' or tipoCarne == 'a':
    if kilos <= 5:
        preco = kilos * 5.90
    if kilos > 5:
        preco = kilos * 6.80
    if pagamento == 'C' or pagamento == 'c':
        desconto = (preco * 5) / 100
        precoAtual = preco - desconto
    elif pagamento == 'D' or pagamento == 'd':
        desconto = 0
        precoAtual = preco
    else:
        print("Digite a forma de pagamento correta!")
        exit()
    print("Tipo de carne: Alcatra")
    print("Quantidade:", round(kilos, 2))
    print("Preço Total:", round(preco, 2))
    print("Tipo de pagamento:", pagamento)
    print("Desconto:", round(desconto, 2))
    print("Valor a pagar:", round(precoAtual, 2))
elif tipoCarne == 'P' or tipoCarne == 'p':
    if kilos <= 5:
        preco = kilos * 6.90
    if kilos > 5:
        preco = kilos * 7.80
    if pagamento == 'C' or pagamento == 'c':
        desconto = (preco * 5) / 100
        precoAtual = preco - desconto
    elif pagamento == 'D' or pagamento == 'd':
        desconto = 0
        precoAtual = preco
    else:
        print("Digite a forma de pagamento correta!")
        exit()
    print("Tipo de carne: Picanha")
    print("Quantidade:", round(kilos, 2))
    print("Preço Total:", round(preco, 2))
    print("Tipo de pagamento:", pagamento)
    print("Desconto:", round(desconto, 2))
    print("Valor a pagar:", round(precoAtual, 2))
else:
    print("Digite o tipo de carne correto!")
    exit()
print()