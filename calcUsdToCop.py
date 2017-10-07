# -*- coding: utf-8 -*-

def usd_to_cop(usd):
	return usd * 3000

def exe():
	print("CALCULADORA U S D to C O P")
	print("")
	usd = float(input("Ingrese los dolares a convertir: "))
	cop = usd_to_cop(usd)
	print("${} dolares equivalen a ${} pesos colombianos".format(usd,cop))

if __name__ == '__main__':
	exe()