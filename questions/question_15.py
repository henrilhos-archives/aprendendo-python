#!/usr/bin/python
# -*- coding: utf-8 -*-

# 15. Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não
# é suficientemente longa. Assumindo que seja possível medir sua sombra e a do
# prédio no chão, e que você lembre da sua altura, faça um programa para ler os
# dados necessários e calcular a altura do prédio.

sombraPessoa = input("Insira a altura da sombra da pessoa: ")
sombraPredio = input("Insira a altura da sombra do prédio: ")
alturaPessoa = input("Insira a altura da pessoa: ")

alturaPredio = (float(alturaPessoa) * float(sombraPredio)) / float(sombraPessoa)

print("\nA altura do prédio é igual a: " + str(alturaPredio))
