# Historias-de-la-Epoca-Medieval-Europea-por-region-y-etapa
"""
Contexto:
Este proyecto tiene como función ser una especie de base de datos para relatos sean ficticios o reales de la época medieval europea. El usuario, puede guardar las anecdotas que más le fascinen, para despues volver a abrirlas y leer lo que dicen. El usuario tiene como responsabilidad de escribir (tomar notas) de los sucesos. Cada una de ellas se va guardando como archivo de texto. El usuario las podrá clasificar por etápa de la época y por región del continente, que serán devueltas junto con el numbre del texto para especificar de que trata.

Algoritmo general:
1. Desde main() se presenta un menu (iniciar()) para escoger si se escribirá texto nuevo, si se abre la biblioteca (con archivos previamente escritos) o si se cierra el programa definitivamente, esta última opción hará que todo el programa se cierre el programa. Para Crear un archivo de texto se selecciona la primera opcion "1. Escribir nuevo archivo".
2. En main() se llama a archivo() que crea una lista a ser llendada con variables. El usuario escribe el nombre que quiere que trate su texto, (el programa acepta mayúsculas y espacios, no acentos). Se puede escoger si es leyenda o no (agregandose como etiqueta).
3. Dentro de la misma función de archivo() se hace referencia a la función crearArchivo(titulo). se abre el archivo en modo escritura, usando el nombre que antes se dio anteriormente y el usuario puede escribir parrafos como el cuerpo del texto desde otra función texto() que la llama desde crearArchivo(). Devuelve a función archivo() lo que se creó.
4. De nuevo en archivo(), se ejecutan las función tagEpoca() y tagRegion() para guardarse como variables. Ahí mismo se también se van añadiendo (en la lista que representa) las demás variables como nombre del archivo y texto, etiquetas.
5. Recordando que archivo() devuelve una lista con los datos, esta se devuelve a main() de donde fue llamada como una variable "historia" la que se añadirá a otra lista que funciona como librería llamando a una función que la crea libreria(), creando así una matriz (lista de listas), para poder ser llamado después.
6. El proceso de crear un archivo y guardar su información se repite cada vez que se escoge "1. Escribir nuevo archivo" como al principio. Se usa tantas veces que se quiera incluso después de escoger la segunda opción "2. Iniciar librería". Como la matriz de biblioteca está afuera de los ciclos, no se modifica la información ya guardada.
7. Si se escogiera la segunda opción ya con textos guardados , el programa mostrara el titulo del archivo junto con sus etiquetas (época, región y/o leyenda), una "historia" a la vez imprime el nombre del texto, su época y región, usando un bucle for con la lista (matriz) de librería. El usuario decide saltarse el archivo para mostrar el siguiente en la lista o si abre ese mismo. Para eso indica "¿Abrir el documento en modo lectura? Presionar "s" para confirmar, enter para saltar:".
8. Si el usuario presiona "s", se llama a la función de lectura(nombre) con el título en mínusculas y sin espacios que se había ocupado antes para abrir el archivo de texto en modo lectura.
9. Después muestra el siguiente documento disponible, y el usuario vuelve a tomar la misma desición.
10. Cuando no haya más archivos que mostrar, el usuario puede volver a escribir más y repetir el proceso.

---- Algoritmo por función ----
def libreria():
  1. Crea y devuelve una lista vacía

def main():
  1. Una variable (lista_libreria) trae la lista vacía de librería
"""
