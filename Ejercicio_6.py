
def C_Edad():
	a_curso=int(input("Ingresa el año en curso: "))
	for i in range(3):
		nombre=input("Nombre de la persona: ")
		nacimiento=int(input("Año de Nacimiento: "))
		
		
		print(nombre, "cumple",(a_curso-nacimiento), " años en el ", a_curso)
        

C_Edad()
