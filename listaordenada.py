# -*- coding:utf-8 -*-

def find_list(number_to_find, list1, low, high):
	if low > high:
		return False

	operation = (low + high) / 2

	if list1[operation] == number_to_find:
		return True
	elif list1[operation] > number_to_find:
		return find_list(number_to_find,list1,low, operation - 1)
	else:
		return find_list(number_to_find,list1,operation + 1, high)

def main():

	list1 = [1,3,5,7,9,10,12,13,14,15,16,17,18,20]
	number_to_find = int(raw_input("Ingresa un número a buscar dentro de la lista: "))
	result = find_list(number_to_find, list1, 0, len(list1) - 1)
	if result == True:
		print("El número si se encuentra en la lista.")
	else: 
		print("El número no se encuentra en la lista.")

if __name__=='__main__':
	main()