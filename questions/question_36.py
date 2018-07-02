#!/usr/bin/python
# -*- coding: utf-8 -*-

# 36. Em uma certificação são feitos são feitos 5 exames (I, II, III, IV e V).
# Escreva um programa que leia as notas destes exames e imprima a classificação
# do aluno, sabendo que a média é 70.

class exames:
    nota1 = input("Informe a nota do exame I: ")
    nota2 = input("Informe a nota do exame II: ")
    nota3 = input("Informe a nota do exame III: ")
    nota4 = input("Informe a nota do exame IV: ")
    nota5 = input("Informe a nota do exame V: ")

ex = exames()

somaExames = float(ex.nota1) + float(ex.nota2) + float(ex.nota3) + float(ex.nota4) + float(ex.nota5)
media = float(somaExames) / 5

if (float(media) >= 70):
    print("\nO estudante passou.")
else:
    print("\nO estudante reprovou.")
