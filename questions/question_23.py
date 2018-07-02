#!/usr/bin/python
# -*- coding: utf-8 -*-

# 23. Escreva um programa que leia um número e imprima se este número é ou não par.

numero = input("Insira um número: ")

resto = float(numero) % 2

if resto == 0:
    print("\nO número é par.")
else:
    print("\nO número é ímpar.")
