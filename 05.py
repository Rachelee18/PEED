"""Crie um programa que leia um numeri do usuário e determine se esse número é par ou ímpar"""

print("Digite um numero: ")
x = int(input(""))

if (x % 2) == 0:
    print(x, "é par")
else:
    print(x, "é impar")