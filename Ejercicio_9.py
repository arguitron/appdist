def contar_vocales(cadena):
	cadena=cadena.lower()
	vocales="aeiou"
	
	for x in vocales:
		contador=0
		for i in cadena:
			if i==x:
				contador+=1
		print("Hay ",contador, " vocales ",x)
				
a=("HOLA pao")
contar_vocales(a)		
