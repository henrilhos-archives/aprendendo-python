#!/usr/bin/python
# -*- coding: utf-8 -*-

# 10. Converter um inteiro informado menor que 32 para sua representação em binário

num = input("Informe um número inteiro menor que 32: ")
cont = 0

if int(num) <= 32:
    bin = bin(int(num))
    print("\nValor em binário: " + str(bin))
else:
    print("\nNúmero inválido.")
