"""
	archivo¨: problema2.py
	Ejemplo de lenguaje Python
	autor:@David
"""
# Pidiendo los valores de las varialbes x,y,z
x = input("Ingrese el valor de x \n")
y = input("Ingrese el valor de y \n")
z = input("Ingrese el valor de z \n");
      
# Realizando los procesos

m1= float(x)+ float(y)/float(z)
m2= float(x)-float(y)/float(z); 
m = m1 / m2
        
# Presentacion de resultados

print("El valor de m, en base a las variables:\nx =%s\n y=%s \n   z=%s\nda como resultado:\n\tm=%.2f"%(x,y,z,m));