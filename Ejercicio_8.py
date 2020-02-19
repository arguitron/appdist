def Nombre():
	x=int(input("Cuantos Nombres Quieres Ingresar? "))
	lista=[]
	for i in range(x):
		a=input("Ingrese el nombre: ")
		lista.append(a)
	print("lista:", lista[0:x])
	comienzo=input("Con que letra empieza el nombre?: ")
	cont=0
	for i in lista:
		if i[0]==comienzo.lower() or i[0]==comienzo.upper():
			cont+=1
	print(cont," Nombres Tienen esa Inicial")
	
Nombre()		
