#escreva um programa que solicita ao usuario um numero inteiro N e imprime todos os numeros de Harshad de 1 a N, um numero de harshad é aquele que é divisivel pela soma dos seus digitos.

num = int(input("Digite um número inteiro: "))
print("Números de Harshad abaixo, de 1 a", num, ":")
for valor in range(1, num +1 ):
    if valor % sum(map(int, str(valor))) == 0:
        print(valor)
