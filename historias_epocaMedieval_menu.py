"""
siglos = [[I,II,III,IV,V,VI,VII,VIII,IX,X][XI,XII,XIII,XIV,XV,]]
epocas = [alta,baja]
personajes = [militares,gobernantes,religiosos]
regiones = [norte,este,oeste,mediterraneo,centro]
"""
def anadir(a):
    if a != "0":
        print("se muestran los items que cumplan con la(s) categorías seleccionadas")
    return a

def primeraSeleccion(a):
    categorias = ["personajes","regiones","leyendas"]
    # Época seleccionado:
    if a == "épocas":
        categorias.insert(0,"siglos")
    #Siglo seleccionado es la lista default, no se añade ni quita
    # Personajes seleccionado:
    if a == "personajes":
        del categorias[0]
        categorias.insert(0,"épocas")
        categorias.insert(1,"siglos")
    # Regiones seleccionado:
    elif a == "regiones":
        del categorias[1]
        categorias.insert(0,"épocas")
        categorias.insert(1,"siglos")
    # Leyendas seleccionado:
    elif a == "leyendas":
        categorias.insert(0,"épocas")
        categorias.insert(1,"siglos")
        del categorias[-1]
        
    otraCategoria = input("Añadir otra categoría? (Presionar 0 para añadir otra, cualquier otra tecla para no): ")
    anadir(otraCategoria)
    for i in range(len(categorias)):
        print(str(i +1) + ". " + categorias[i])
    

def menuCategorias(): # menu incial (muestra todas las categorías)
    print("1. Épocas")
    print("2. Siglos")
    print("3. Tipos de personajes")
    print("4. Regiones")
    print("5. Leyendas")
    print("6. Salir")

def main():
    # se abre ciclo while para repeticiones
    menuCategorias()
    primeraSeleccion = True
    while primeraSelección:
    opcion = int(input("Opcion: "))
        # Primera selección
        if opcion == 1: 
            primeraSeleccion("épocas") #excluye epocas, incluye lo demás
        elif opcion == 2:
            primeraSeleccion(opcion) # excluye tiempos, incluye lo demás
        elif opcion == 3:
            primeraSeleccion("personajes") # excluye personajes
        elif opcion == 4:
            primeraSeleccion("regiones") #excluye regiones
        
        elif opcion == 5:
            listaCategorias("leyendas") #exclue leyendas
        elif opcion == 6:
            print("Adios")
        primeraSeleccion = False

main()
