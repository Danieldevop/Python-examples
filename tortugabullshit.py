# -*- coding: utf-8 -*-
import turtle  

window = turtle.Screen()
dave = turtle.Turtle()

def square(dave):
	lenght = int(input("Defina el tamaño del cuadrado: "))
	for i in range(4):
		dave.forward(lenght)
		dave.left(90)

square(dave)
turtle.mainloop()