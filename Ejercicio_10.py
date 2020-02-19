def es_bisiesto():
	print("Comprueba años bisiestos")
	a=int(input("Escriba un año: "))
	if a%4==0 and (not(a%100==0)):
		print("El año ",a, " es un año bisiesto")
	elif a%400==0:
		print("El año ",a, " es un año bisiesto")
	else:
		print("El año ",a, " no es un año bisiesto")
		
es_bisiesto()
