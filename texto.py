import binascii

#texto = "hola mundo"
texto = input("Ingresar texto: ") #o reemplazar por 'abrir texto'

def convertirTextoAbytes():
    global texto
    return ''.join(format(ord(x), 'b') for x in texto) #cambiar '' por ' ' para que separee cada caracter(?)


"""
def convertirTextoAHex():
    texto = bytes("hola mundo")
    binascii.hexlify(b'{""}').format(texto)
"""


print(convertirTextoAbytes())