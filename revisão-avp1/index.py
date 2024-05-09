"""
Dados 3 números, determina quem é o Menor
2. Escreva um programa que peça ao usuário para digitar um caractere everifique se ele é uma consoante.
3. Criar um programa para calcular o IMC (Índice de Massa Corporal) de umapessoa. Classifique o usuário de acordo com a tabela de IMC
4. Faça um programa que peça dois números ao usuário e exiba qual deles é o menor. Se forem iguais, exiba uma mensagem indicando isso.
5. Faça uma programa que recebe 2 notas (avp1 e avp2). Calcule a média einforme se o aluno foi aprovado, reprovado ou avf.
6. Entre com um número e imprimir umas das mensagens: “é múltiplo de 15” ou“não é múltiplo de 15”
"""
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 and num1 > num3:
    print(num1, "é o maior")
elif num2 > num1 and num2 > num3:
    print(num2, "é o maior")
elif num3 > num1 and num3 > num2:
    print(num3, "é o maior")
else:
    print("são iguais")
    """
"""
char = input()
vogais = ["a", "e", "i", "o","u"]
if char in vogais:
    print(char, "não é uma consoante")
else:
    print(char, "é uma consoante")
    """
"""
altura = float(input())
peso = float(input())
imc = (peso/ altura) * 2
print(f"{imc:.2f}")
"""
"""
num = int(input())
num2 = int(input())
if num < num2:
    print(num, "é o menor")
elif num2 < num:
    print(num2, "é o menor")
else: 
    print("sao iguais")
    """
"""
nota1 = int(input())
nota2 = int(input())
media = (nota1 + nota2)/2
if media >= 7:
    print("aprovado")
elif media >= 4:
    print("avf")
else:
    print("reprovado")
    """
"""
num = int(input())
if num % 15 == 0:
    print("multiplo de 15")
else: 
    print("nao")
    """
