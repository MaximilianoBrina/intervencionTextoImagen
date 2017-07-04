a=list([letra for letra in rango] for rango in (reversed(rangoDeLetrasAZminuscula(5))))
b=[''.join(letra) for letra in list([letra for letra in rango] for rango in (reversed(rangoDeLetrasAZminuscula(5))))]
#a=list([letra for letra in rango] for rango in (reversed(rangoDeLetrasAZminuscula(5))))
#b=[''.join(letra) for letra in a

print(a)
print(b)

#print(a[0][0])
#print(a[1][0])

"""###
lista = []
for palabra in ("hola", "mundo"):
    lista.append(palabra.split(","))

print(lista)


a="hola"
print(a.split())"""
