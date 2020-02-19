def c_mayusculas(cadena):
	cont=0
	for i in cadena:
		if i != i.lower():
			cont += 1
	print ("La cadena tiene ",cont," Mayusculas")

a=("Iniciando Programa FALLOUT")

c_mayusculas(a)
