#!/usr/bin/python
# -*- coding: utf-8 -*-

# 24. Escreva um programa que leia três números e mostre o maior entre eles.

num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")
num3 = input("Insira o terceiro número: ")

if (float(num1) > float(num2)) and (float(num1) > float(num3)):
    print("\nO valor " + str(num1) + " é o maior.")
elif (float(num2) > float(num1)) and (float(num2) > float(num3)):
    print("\nO valor " + str(num2) + " é o maior.")
else:
    print("\nO valor " + str(num3) + " é o maior.")
