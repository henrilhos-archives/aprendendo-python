#!/usr/bin/python
# -*- coding: utf-8 -*-

# 11. Faça um algoritmo para calcular a nota semestral de um aluno. A nota
# semestral é obtida pela média aritmética entre a nota de 2 bimestres. Cada
# nota de bimestre é composta por 2 notas de provas.

class bim1:
    nota1 = input("Informe a 1ª nota do 1º bimestre: ")
    nota2 = input("Informe a 2ª nota do 1º bimestre: ")
class bim2:
    nota1 = input("\nInforme a 1ª nota do 2º bimestre: ")
    nota2 = input("Informe a 2ª nota do 2º bimestre: ")

b1 = bim1()
b2 = bim2()

media1 = (float(b1.nota1) + float(b1.nota2)) / 2
media2 = (float(b2.nota1) + float(b2.nota2)) / 2

mediaSem = (float(media1) + float(media2)) / 2

print("\nA média semestral é: " + str(mediaSem))
