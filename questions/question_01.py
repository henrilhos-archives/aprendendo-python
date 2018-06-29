#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1. Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perímetro.

base = input("Informe a base: ")
altura = input("Informe a altura: ")

area = (base * altura)
perimetro = (base * 2) + (altura * 2)

print("\nÁrea: " + str(area))
print("Perímetro: " + str(perimetro))
