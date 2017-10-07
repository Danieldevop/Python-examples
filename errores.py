# -*- coding:utf-8 -*-

FLAG = ['''

     o____  
     |\\//|	
     |//\\|	
     |		

''']
countries = {
	
	"mexico": 122,
	"colombia":49,
	"argentina":43,
	"chile":18,
	"peru":31 
}

while True:
	print(FLAG[0])
	print('')
	country = str(raw_input("Escribe nombre de un pais: ")).lower()
	print("Para salir escribe (S)")
	try:
		print("la poblacion de {} es {} millanes".format(country, countries[country]))

	except KeyError:
		print("No tenemos el dato de la poblacion de {}".format(country))
		print("Para salir escribe (S)")

	if country == "s":
		print("ADIOS!")
		break