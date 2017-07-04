texto = input("Ingresar texto: ") #reemplazar por 'abrir texto'


def convertirTextoAbytes():
    global texto
    textoBinario = ''.join(format(ord(x), 'b') for x in texto)
    textoBinario2 = [int(b, 2) for b in textoBinario]
    pepe = ''.join(map(str, textoBinario2))
    pepe2=hex(int(pepe))
    print(pepe2)

    with open("imagen - copia - copia (11).jpg", 'r+b') as archivo:
        archivo.seek(1000)###TRANSFORMAR ESTO QUE SE VE EN EL EDITOR HEX
        archivo.write(bytearray(pepe2, 'utf8'))

#200-300-250-251-256-265-400-500-700
#no:100-150-243
convertirTextoAbytes()
#print(hex(int(pepe,2)))
