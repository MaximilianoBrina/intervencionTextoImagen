import texto

def intervenirImagenConTexto():
    with open("imagen.jpg", "rb+") as binario:
        binario.write(bytearray(texto.convertirTextoAbytes()))
        #binario.write(bytes(convertirTextoABts(), "UTF-8")) # v2 tampoco
