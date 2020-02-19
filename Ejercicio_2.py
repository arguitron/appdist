def mas_larga(lista):
	mas_larga=""
	for i in lista:
		if len(i)>len(mas_larga):
			mas_larga=i
	return mas_larga
	
a=("hola como  estas amigo chams")
b=("hola como  estas amigo")
c=("esta cadena tiene mas caracteres que las demas.")
d=[a,b,c]
	
print(mas_larga(d))
