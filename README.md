# Historias-de-la-Epoca-Medieval-Europea-por-region-y-etapa
"""
Este proyecto tiene como propósito dar a conocer mitos, leyendas e historias verdaderas de la época medieval en Europa seleccionando por tópicos, año y regiones. Se enfoca en dar opciones de selección implementando ciertos modelos mixtos. Tiene un enfoque meramente de entretenimiento para los fanáticos de la historia, especialmente de la época medieval.

Cada artículo será categorizado. EL usuario podrá seleccionar de una a varias categorías y el programa presentará los artículos que cumplen con las categorías seleccionadas. Las categorías que se pueden seleccionar son:
  - Ficción / no ficción
  - Tipos de personajes
  - Regiones
  - Siglos
  - Etápas
"""
"""
siglos = [[I,II,III,IV,V,VI,VII,VIII,IX,X][XI,XII,XIII,XIV,XV,]]
epocas = [alta,baja]
personajes = [militares,gobernantes,religiosos]
regiones = [norte,este,oeste,mediterraneo,centro]
"""

# arreglar coso de aparición de epocas y siglos
def categories(seleccion):
    categorias = ["epocas","siglos","personajes","regiones","leyendas"]
    if seleccion == 1:
        if categorias[0] == "epocas": # Quitando epocas, fue ya seleccionado
            del categorias[0]
        elif categorias[0] == "siglos": # Quitando siglos, fue ya seleccionado
            del categorias[0]
        elif categorias[-1] == "leyendas": # Quitando leyendas ya que es no ficción
            del categorias[-1]
        for i,item in enumerate(categorias):
            print(str(i+1)+". " + item) # enumera opciones restantes

    elif seleccion == 2:
        if categorias[0] == "epocas": #Quitando epocas porque siglos forma parte de
            del categorias[0]
        elif categorias[0] == "siglos": # Quitando siglos, fue ya seleccionado
            del categorias[0]
        if categorias[-1] == "leyendas": # Quitando leyendas ya que es no ficción
            del categorias[-1]
        for i,item in enumerate(categorias):
            print(str(i+1)+". " + item)
    
    elif seleccion == 3:
        del categorias[2] #Quitando opcion ya seleccionada
        if categorias[-1] == "leyendas": # Quitando por que es no ficción
            del categorias[-1]
        for i,item in enumerate(categorias):
            print(str(i+1)+". " + item)

    elif seleccion == 4:
        del categorias[3] #Quitando opcion ya seleccionada
        for i,item in enumerate(categorias):
            print(str(i+1)+". " + item)
    
    elif seleccion == 5:
        del categorias[0:3]
        print(categorias[:])

    print(categorias[:])
    return categorias
    

def menuCategorias(): # menu incial (muestra todas las categorías)
    print("1. Épocas")
    print("2. Siglos")
    print("3. Tipos de personajes")
    print("4. Regiones")
    print("5. Leyendas")

def main():

        menuCategorias()
        opcion = int(input("Seleccione una categoría: "))

        otra = int(input("Añadir categoría?(Presionar '1' para si, presonar cualquier otra tecla para no): "))
        while otra == 1: #se añaden más categorías
            categories(opcion)
            seleccion = int(input("Seleccione una categoría: "))
            categories(opcion)
            input("Añadir categoría?(Presionar '1' para si, presonar cualquier otra tecla para no): ")
        if otra != 1:
            print ("Adios")
            continuar = False

            
            # se van seleccionando categorías


main()
