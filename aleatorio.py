# -*- coding: utf-8 -*-
import random

def num_aleatorio(num_ini, num_fin):
	aleatory_number = random.randint(num_ini, num_fin)
	number_found = False
	while not number_found:
		number = int(raw_input("Intenta un número: "))

		if number == aleatory_number:
			print("felicidades. encontraste el número")
			number_found == True
		elif number > aleatory_number:
			print("el número es mas pequeño")
		else:
			print("el número es mas grande")
def correr():
	num_ini = int(raw_input("ingresa el numero inicial aleatorio: "))
	num_fin = int(raw_input("ingresa número final aleatorio: "))
	num_aleatorio(num_ini, num_fin)

if __name__ == '__main__':
	correr()
