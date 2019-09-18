# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 69. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
n = int(input("Escreva um número:"))
if n < 0:
    print("O número deve ser positivo!")
    exit()
for i in range(1, n + 1):
    if i == 2 or (i != 1 and i % 2 == 1):
        print(i, "é primo!")
    else:
        print(i, "não é primo!")
print()

# 70. Faça um programa que calcule o mostre a média aritmética de N notas.
quantidade = int(input("Quantas notas serão informadas?"))
listaQtd = []
listaNotas = []
while quantidade > 0:
    nota = int(input("Informe a nota:"))
    listaQtd.append(quantidade)
    listaNotas.append(nota)
    quantidade -= 1
media = sum(listaNotas) / len(listaQtd)
print("A média das notas é de:", round(media, 2))
print()

# 71. Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
nPessoas = int(input("Quantas pessoas tem na turma?"))
listaPessoas = []
listaIdade = []
while nPessoas > 0:
    idade = int(input("Idade da pessoa:"))
    listaPessoas.append(nPessoas)
    listaIdade.append(idade)
    nPessoas -= 1
classe = sum(listaIdade) / len(listaPessoas)
if 0 <= classe <= 25:
    print("A turma é Jovem!")
elif 26 <= classe <= 60:
    print("A turma é Adulta!")
else:
    print("A turma é Idosa!")
print()

# 72. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
eleitores = int(input("Informe o número de eleitores:"))
a = 0
b = 0
c = 0
for i in range(1, eleitores + 1):
    print("Digite A, B ou C para votar no respectivo candidato")
    voto = input("Letra do candidato:")
    if str.upper(voto) == 'A':
        a += 1
    elif str.upper(voto) == 'B':
        b += 1
    elif str.upper(voto) == 'C':
        c += 1
    else:
        print("A letra do canditado não foi inserida corretamente!")
        break
print("O candidato A recebeu:", a, "votos de", eleitores)
print("O candidato B recebeu:", b, "votos de", eleitores)
print("O candidato C recebeu:", c, "votos de", eleitores)
print()

# 73. Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
import math
turmas = int(input("Informe a quantidade de turmas:"))
listaAlunos = []
for i in range(1, turmas + 1):
    alunos = int(input("Informe a quantidade de aluno na turma:"))
    listaAlunos.append(alunos)
    if alunos > 40:
        print("Cada turma deve conter 40 alunos no máximo!")
        exit()
mediaAlunos = sum(listaAlunos) / turmas
print("A média de aluno por turma é de:", math.ceil(mediaAlunos))
print()