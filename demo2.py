"""
	archivo¨: demo2.py
	Ejemplo de lenguaje Python
	autor: @David
"""

import sys

variable = sys.argv[0]
dato1 = sys.argv[1]
dato2 = sys.argv[2]

#Realizando las operaciones

suma = int(dato1) + int(dato2)
mult = int(dato1) * int(dato2)

#Mostrando los resultados

print ("La suma es de:	%s" % suma)
print ("La multiplicacion es de:  %s" % mult)
