def mayora20(tup):
	cont=0
	for i in tup:
		if i>20:
			cont +=1
	print("Hay ",cont, " numeros mayores a 20")
	
a=[3,4,5,9,25]
mayora20(a)
