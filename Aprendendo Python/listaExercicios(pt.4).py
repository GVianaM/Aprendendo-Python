# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 19. Faça um Programa que peça dois números e imprima o maior deles.
num1 = float(input("Escreva um número:"))
num2 = float(input("Escreva outro número:"))
if num1 > num2:
    print(num1, "é o maior número")
else:
    print(num2, "é o maior número")
print()

# 20. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
x = float(input("Escreva um número:"))
if x > 0:
    print(x, "é um número positivo")
elif x < 0:
    print(x, "é um número negativo")
else:
    print(x, "é um número neutro")
print()

# 21. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input("Escreva a inicial do seu sexo:"))
if sexo == "F" or sexo == "f":
    print("F - Feminino")
elif sexo == "M" or sexo == "m":
    print("M - Masculino")
else:
    print("Sexo inválido")
print()

# 22. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input("Escreva uma letra:"))
vogal = ['a', 'e', 'i', 'o', 'u', 'y']
if letra in vogal:
    print(letra, "é uma vogal")
else:
    print(letra, "é uma consoante")
print()

# 23. Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input("Escreva a primeira nota:"))
nota2 = float(input("Escreva a segunda nota:"))
media = (nota1 + nota2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
print()

# 24. Faça um Programa que leia três números e mostre o maior deles.
x = float(input("Escreva um número:"))
y = float(input("Escreva mais um número:"))
z = float(input("Escreva outro número:"))
if x > y and x > z:
    print(x, "é o maior número")
elif y > x and y > z:
    print(y, "é o maior número")
elif z > x and z > y:
    print(z, "é o maior número")
else:
    print("Escreva números diferentes!")
print()