#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ler dois números inteiros e exibir o quociente e o resto da divisão inteira entre eles.

num1 = input("Informe o 1º número inteiro: ")
num2 = input("Informe o 2º número inteiro: ")

quociente = int(num1) / int(num2)
resto = int(num1) % int(num2)

print("\nQuociente: " + str(quociente))
print("Resto: " + str(resto))
