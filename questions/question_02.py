#!/usr/bin/python
# -*- coding: utf-8 -*-

# 2. Dado o tamanho do lado de um quadrado, calcular a área e o perímetro do mesmo.

lado = input("Informe a medida do lado: ")

area = lado ** 2
perimetro = lado * 4

print("\nÁrea: " + str(area))
print("Perímetro: " + str(perimetro))
