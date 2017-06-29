
# imagen
imagen = open("imagen.jpg", 'rb')
imagenBinario = imagen.read()
imagen.close()

# txt
texto = open("texto.txt", 'rb')
textoBinario = texto.read()
texto.close()

# Combine the files
archivoCombinado = open('archivoCombinado.jpg', 'wb')
archivoCombinado.write(imagenBinario)
archivoCombinado.write(textoBinario)
archivoCombinado.close()

#comparar  ##   PROBAR DIFFLIB
print(len(imagenBinario))
print(len(textoBinario))
archivoCombinado = open('archivoCombinado.jpg', 'rb')
archivoCombinadoBinario = archivoCombinado.read()
archivoCombinado.close()
print(len(archivoCombinadoBinario))

#recuperar el texto??
print(imagenBinario)

print(archivoCombinadoBinario)
