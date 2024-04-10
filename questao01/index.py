#Escreva um programa que solicita ao usuario um numero inteiro N e imprime todos os numeros primos de 1 a N.
numero = int(input("Digite um número inteiro positivo: "))
print("Números primos de 1 a", numero, ":")
for num in range(2, numero + 1):
    if all(num % i != 0 for i in range(2, num)):
        print(num)
