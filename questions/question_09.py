#!/usr/bin/python
# -*- coding: utf-8 -*-

# 9. Faça um algoritmo que calcule e apresente o valor do volume de uma lata de
# óleo, dado seu raio e sua altura.

pi = 3.14

raio = input("Informe o raio da lata de óleo: ")
altura = input("Informe a altura da lata de óleo: ")

volume = pi * (float(raio) ** 2) * float(altura)

print("\nO volume da lata de óleo é de: " + str(volume))
