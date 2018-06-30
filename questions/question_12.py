#!/usr/bin/python
# -*- coding: utf-8 -*-

# 12. Faça um algoritmo que transforme uma velocidade fornecida em m/s pelo
# usuário para Km/h. Para tal, multiplique o valor em m/s por 3,6.

ms = input("Informe a velocidade em m/s: ")

kmh = float(ms) * 3.6

print("A velocidade em km/h é de: " + str(kmh))
