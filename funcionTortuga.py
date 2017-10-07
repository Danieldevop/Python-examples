# -*- coding: utf-8 -*-
import turtle 

def main():
	window = turtle.Screen()
	dave = turtle.Turtle()
	make_square(dave)
	turtle.mainloop()

def make_square(dave):
	lenght = int(input("Defina el tamaño del cuadrado: "))
	for i in range(4):
		dave.forward(lenght)
		dave.left(90)

if __name__ == '__main__':
	main()

