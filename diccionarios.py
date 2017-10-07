calificaciones = {}
calificaciones["algoritmos"] = 9
calificaciones["matematicas"] = 10
calificaciones["web"] = 8
calificaciones["bases de datos"] = 10

suma_calificaciones = 0

for calificacion in calificaciones.values():
	suma_calificaciones += calificacion

promedio = suma_calificaciones / len(calificaciones.values())
print(promedio)
