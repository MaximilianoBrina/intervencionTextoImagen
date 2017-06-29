import binascii

#archivo = imagen.jpg # asignar archivo a variable?

def comprobarEsJPG():
    #global archivo
    jpg = [binascii.unhexlify(b'FFD8FFD8'), binascii.unhexlify(b'FFD8FFE0'), binascii.unhexlify(b'FFD8FFE1')]

    with open("imagen.jpg", 'rb') as archivoBinario: #reemplazar por funcion que cargue archivo etc
        cuatrobytes = archivoBinario.read(4)
        if cuatrobytes in jpg:
            abrirImagenComoBinario() #print("si")
        else:
            print("Formato de imagen invalido. Debe ser JPG")

def abrirImagenComoBinario():
    with open("imagen.jpg", "rb") as binario:
        imagenBinario = binario.read()
        ###SACAR###
        print(imagenBinario)
        binario.seek(0)
        primerosCuatrobytes = binario.read(4)
        print(primerosCuatrobytes)
        ###########
        #ESCRIBIR EL TEXTO EN LA IMAGEN / intervenirImagenConTexto.intervenirImagenConTexto()

