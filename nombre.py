# -*- coding: utf-8 -*-

x = int(raw_input("escribe un número: "))
y = int(raw_input("escribe otro número "))
name =  raw_input("cuál es tu nombre?")
if (name == "daniel"):
	suma = x  + y
	print("hola " + name + "!")
	print("la suma de los números es: " + str(suma))

else:
	print("no has puesto el nombre correcto!!!")