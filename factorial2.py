# -*- coding:utf-8 -*-
import math
def factorial_of_number(enterNumber):
	return math.factorial(enterNumber)

if __name__ == '__main__':

	enterNumber = int(raw_input("Ingresa un número para obtener su factorial: "))
	result =  factorial_of_number(enterNumber)
	print("El factorial de {} es {}".format(enterNumber,result))
