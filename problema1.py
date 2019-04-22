"""
	archivo¨: problema1.py
	Ejemplo de lenguaje Python
	autor:@David
"""

# Pidiendo los datos del costo por hora y cantidad de horas trabajadas

costohora = input("Ingrese el precio que cobra por hora \n")
numhoras = input ("Ingrese el numero de horas que trabaja \n")

#Realizando los calculos

pagosinsegu = float(costohora) * float(numhoras)
suelmensual = float(pagosinsegu) * 0.10
sueltotal = pagosinsegu - suelmensual

# Presentando los resultados

print("Su sueldo mensual es de: %.2f"% sueltotal)