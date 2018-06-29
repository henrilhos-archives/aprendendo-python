#!/usr/bin/python
# -*- coding: utf-8 -*-

# 7. Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias.

anos = 0
meses = 0
cont = 1

dias = input("Informe a idade em dias: ")

while int(cont) <= int(dias):
    if int(dias) >= 365:
        anos = int(anos) + 1
        dias = int(dias) - 365
    if int(dias) >= 30:
        meses = int(meses) + 1
        dias = int(dias) - 30
        if int(meses) == 12:
            anos = int(anos) + 1
            meses = int(meses) - 12
    cont = int(cont) + 1

print("\nA pessoa tem " + str(anos) + " ano(s), " + str(meses) + " mes(es) e " + str(dias) + " dia(s)")
