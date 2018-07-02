#!/usr/bin/python
# -*- coding: utf-8 -*-

# 21. Escreva um programa que leia um número e exiba se ele é positivo ou
# negativo.

num = input("Digite um número: ")

if (int(num) > 0):
    print("\nVocê digitou um número positivo.")
elif (int(num) < 0):
    print("\nVocê digitou um número negativo.")
else:
    print("\nVocê digitou o número zero.")
