#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3. Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro da mesma.

pi = 3.14

raio = input("Informe o raio da circunferência: ")

area = pi * (raio ** 2)
perimetro = 2 * pi * raio

print("\nÁrea: " + str(area))
print("Perímetro: " + str(perimetro))
