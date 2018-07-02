#!/usr/bin/python
# -*- coding: utf-8 -*-

# 18. Escreva um programa que permute o valor de duas variáveis inteiras.

a = input("Informe o valor de A: ")
b = input("Informe o valor de B: ")

aux = float(a)
a = float(b)
b = float(aux)

print("\nValor de A: " + str(a))
print("Valor de B: " + str(b))
