# -*- coding:utf-8 -*-

def num_primo(number):
	if number / 3 == float:
		print("Tu número no es primo")
	else:
		print("Tu número es primo")


def run():
	number = int(raw_input("Ingresa un número para saber si es primo: "))
	result = num_primo(number)


if __name__ == '__main__':
	run()

