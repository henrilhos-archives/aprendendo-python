#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3. Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro
# da mesma.

pi = 3.14

raio = input("Informe o raio da circunferência: ")

area = int(pi) * (int(raio) ** 2)
perimetro = 2 * int(pi) * int(raio)

print("\nÁrea: " + str(area))
print("Perímetro: " + str(perimetro))
