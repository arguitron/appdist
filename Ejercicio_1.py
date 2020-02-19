def max_in_lista(lista):
	inicio=0
	for i in lista:
		if i>inicio:
			inicio=i
	return inicio

a=[3,4,6,2,56,23,78]
print (max_in_lista(a))
