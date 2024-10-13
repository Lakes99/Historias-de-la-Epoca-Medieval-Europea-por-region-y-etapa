def tagEpoca():
    print()
    print('--- Épocas ---')
    alta = 'Edad Media Alta (s.V - s.X)'
    baja = 'Edad Media Baja (s.XI - XV)'
    lista = [alta,baja]
    print('Opciones:')
    for i in range(len(lista)):
        print(f'{i+1}.',lista[i])
    opcion = int(input('Epoca (Escribir número): '))
    opcion -= 1
    tag = lista[opcion]
    return tag

def tagRegion():
    print()
    print('--- Regiones ---')
    norte = 'Region Norte'
    britanica = 'Islas Británica'
    occidente = 'Region Occidente'
    centro ='RegionCentro'
    oriente = 'Region Oriente'
    sureste = 'Region Sureste'
    sur ='Region Sur'
    lista = [norte,britanica,occidente,centro,oriente,sureste,sur]
    for i in range(len(lista)):
        print(f'{i+1}.',lista[i])
    opcion = int(input('Región (Escribir número): '))
    print()
    opcion -= 1
    tag = lista[opcion]
    return tag

def texto():
    lista = [] #se guardan todos los parrafos
    escrito = None
    print('Para terminar de escribir, teclee "xxx"')
    while escrito != 'xxx':
        escrito = input()
        texto = f'{escrito}\n'
        lista.append(texto)
    return lista

def crearArchivo(titulo):# Crea un archivo
    nombreArchivo = f'{titulo}.txt'
    archivo = open(nombreArchivo, 'w+')
    parrafos = texto() #esto es una lista
    archivo.writelines(parrafos)
    archivo.seek(0)
    archivo.close()
    return archivo

def archivo(): # lista = [nombre de archivo,título,epoca,(leyenda)]
    nombre = input('Título, sin carácteres especiales, espacios y mayusculas permitidos: ')
    veras = input('Presionar "L", si es leyenda, enter para saltar: ' )
    tituloJunto = nombre.replace(' ','')
    tituloJunto = tituloJunto.lower()
    documento = crearArchivo(tituloJunto) #se crea el documento
    partes = []
    epoca = tagEpoca()
    region = tagRegion()
    #se añaden a la lista en ese orden:
    partes.append(tituloJunto)
    partes.append(nombre)
    partes.append(epoca)
    partes.append(region)
    if veras == 'l':
        partes.append('Leyenda')
    return partes

def iniciar():
    print('1. Escribir nuevo archivo')
    print('2. Iniciar libreria')
    print('3. Salir definitivamente')

def lectura(nombre):
    titulo = f'{nombre}.txt'
    archivo = open(f'{titulo}','r+')
    archivo.seek(0)
    contenido = archivo.read()
    print(contenido)
    archivo.close()

def main():
    libreria = []  # Esta es una matriz (lista de listas)
    continuar = True
    while continuar:
        iniciar()
        opcion = int(input('Opción: '))
        if opcion == 1:  # escribe
            historia = archivo()
            libreria.append(historia)
        elif opcion == 2:  # mostrar documentos
            for i in range(len(libreria)):
                print(f'Texto: {libreria[i][1]}')
                for j in range(len(libreria[i])):
                    if j > 1:
                        print(libreria[i][j])
                decision = input('Abrir el documento en modo lectura? Presionar "s" para confirmar, enter para saltar: ')
                if decision == 's':
                    lectura(libreria[i][0])
        elif opcion == 3:  # salir
            continuar = False

main()
