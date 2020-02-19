def filtrar_palabras(lista,n):
	for i in lista:
		if len(i)>n:
			print(i)
     
a=("hola")
b=("fernanda")
c=("hipopotamossss")
d=(a,b,c)
#b=(8,9,7,8,5,0)
m=5
filtrar_palabras(d,8)
