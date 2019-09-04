# O PRINT() ABAIXO DE CADA EXERCICIO SERVE PARA DAR ESPAÇAMENTO DE LINHA NA HORA DE RODAR O PROGRAMA
# 47. Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = float(input("Escreva uma nota entre 0 e 10:"))
while nota < 0 or nota > 10:
    print("Escreva a nota corretamente!")
    nota = float(input("Escreva uma nota entre 0 e 10:"))
print("A nota escrita foi:", nota)
print()

# 48. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
user = input("Escreva o nome de usuário:")
password = input("Escreva a senha:")
while user == password:
    print("O nome de usuário e a senha devem ser diferentes!")
    user = input("Escreva o nome de usuário:")
    password = input("Escreva a senha:")
print("Login feito com sucesso!")
print()

# 49. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd'
nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
salario = float(input("Informe seu salário:"))
print("Abaixo será aceito apenas 'F' de Feminino ou 'M' de Masculino.")
sexo = input("Informe seu sexo:").upper()
print("Digite 'S' para Solteiro, 'C' para Casado, 'V' para Viúvo ou 'D' para Divorciado.")
eC = input("Informe seu estado civil:").upper()
while len(nome) < 3:
    print("O nome precisa conter mais de 3 caracteres.")
    nome = input("Informe seu nome:")
while idade < 0 or idade > 150:
    print("A idade precisa estar entre 0 e 150.")
    idade = int(input("Informe sua idade:"))
while salario < 0:
    print("O salário precisa ser maior que 0.")
    salario = float(input("Informe seu salário"))
while sexo != 'F' and sexo != 'M':
    print("O sexo precisa ser informado com F ou M.")
    sexo = input("Informe seu sexo:").upper()
while eC != 'S' and eC != 'C' and eC != 'V' and eC != 'D':
    print("O estado civil precisa ser informado com S, C, V ou D.")
    eC = input("Informe seu estado civil:").upper()
print("As informações foram validadas! Obrigado.")
print()

# 50. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento
popA = 80000
popB = 200000
anos = 0
while popA < popB:
    popA = popA * 3 / 100
    popB = popB * 1.5 / 100
    anos += 1
print('Para que a população A seja igual a população B serão necessários', anos, 'anos.')
print()

# 51. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
pop1 = int(input("Escreva a população da cidade A:"))
pop2 = int(input("Escreva a população da cidade B:"))
taxa1 = float(input("Escreva a taxa anual de crescimento da cidade A:"))
taxa2 = float(input("Escreva a taxa anual de crescimento da cidade B:"))
anos = 0
while taxa1 < 0 or taxa1 > 100:
    print("A taxa anual precisa ser entre 0 e 100")
    taxa1 = float(input("Escreva a taxa anual de crescimento da cidade A:"))
while taxa2 < 0 or taxa2 > 100:
    print("A taxa anual precisa ser entre 0 e 100")
    taxa2 = float(input("Escreva a taxa anual de crescimento da cidade B:"))
if pop1 < pop2:
    while pop1 < pop2:
        pop1 = pop1 * taxa1 / 100
        pop2 = pop2 * taxa2 / 100
        anos += 1
    print("Para que a população da cidade A seja igual da cidade B serão necessários", anos, "anos.")
elif pop1 > pop2:
    while pop1 > pop2:
        pop1 = pop1 * taxa1 / 100
        pop2 = pop2 * taxa2 / 100
        anos += 1
    print("Para que a população da cidade B seja igual da cidade A serão necessários", anos, "anos.")
else:
    print("A população das cidades são iguais.")
print()