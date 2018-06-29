#!/usr/bin/python
# -*- coding: utf-8 -*-

# 8. Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32),
# ler um valor de temperatura em Fahrenheit e exibi-lo em Celsius

fahrenheit = input("Informe a temperatura em Fahrenheit: ")

celsius = (5 / 9) * (float(fahrenheit) - 32)

print("\nTemperatura em Celsius: " + str(celsius))
