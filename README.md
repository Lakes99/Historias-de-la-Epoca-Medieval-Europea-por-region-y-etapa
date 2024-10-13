# Historias-de-la-Epoca-Medieval-Europea-por-region-y-etapa

Contexto:
Este proyecto tiene como función ser una especie de base de datos para relatos sean ficticios o reales de la época medieval europea. El usuario puede guardar las anécdotas que más le fascinen, para después volver a abrirlas y leer lo que dicen. El usuario tiene como responsabilidad de escribir (tomar notas) de los sucesos. Cada una de ellas se va guardando como archivo de texto. El usuario las podrá clasificar por etapa de la época y por región del continente, que serán devueltas junto con el nombre del texto para especificar de qué trata.


Algoritmo general:

1. El programa empieza llamando a la función main()
Desde main() se presenta un menu (iniciar()) para escoger si se escribirá texto nuevo, si se abre la biblioteca (con archivos previamente escritos) o si se cierra el programa definitivamente, esta última opción hará que todo el programa se cierre el programa. Para crear un archivo de texto se selecciona la primera opción "1. Escribir nuevo archivo".

2. En main() se llama a archivo() que crea una lista a ser llenada con variables. El usuario escribe el nombre que quiere que trate su texto, (el programa acepta mayúsculas y espacios, no acentos). Se puede escoger si es leyenda o no (agregándose como etiqueta).

3. Dentro de la misma función de archivo() se hace referencia a la función crearArchivo(titulo). Se abre el archivo en modo escritura, usando el nombre que antes se dio anteriormente y el usuario puede escribir párrafos como el cuerpo del texto desde otra función texto() que la llama desde crearArchivo(). Devuelve la función archivo() lo que se creó.
De nuevo en archivo(), se ejecutan las función tagEpoca() y tagRegion() para guardarse como variables. Ahí mismo se también se van añadiendo (en la lista que representa) las demás variables como nombre del archivo y texto, etiquetas.

4. Recordando que archivo() devuelve una lista con los datos, esta se devuelve a main() de donde fue llamada como una variable "historia" la que se añadirá a otra lista que funciona como librería llamando a una función que la crea libreria(), creando así una matriz (lista de listas), para poder ser llamado después.

5. El proceso de crear un archivo y guardar su información se repite cada vez que se escoge "1. Escribir nuevo archivo" como al principio. Se usa tantas veces como se quiera incluso después de escoger la segunda opción "2. Iniciar librería". Como la matriz de biblioteca está fuera de los ciclos, no se modifica la información ya guardada.

6. Si se escogiera la segunda opción ya con textos guardados , el programa mostrará el título del archivo junto con sus etiquetas (época, región y/o leyenda), una "historia" a la vez imprime el nombre del texto, su época y región, usando un bucle for con la lista (matriz) de librería. El usuario decide saltarse el archivo para mostrar el siguiente en la lista o si abre ese mismo. Para eso indica "¿Abrir el documento en modo lectura? Presionar "s" para confirmar, enter para saltar:".

7. Si el usuario presiona "s", se llama a la función de lectura(nombre) con el título en minúsculas y sin espacios que se había ocupado antes para abrir el archivo de texto en modo lectura.

8. Después muestra el siguiente documento disponible, y el usuario vuelve a tomar la misma decisión.

9. Cuando no haya más archivos que mostrar, el usuario puede volver a escribir más y repetir el proceso.



Como usar:

1. Correr el programa

2. En el shell aparece un menú

3. Para "Opcion: " teclear '1', dar enter

4. Para 'Título, sin carácteres especiales, espacios y mayusculas permitidos: ', escribir "Juana de Arco" y dar enter

5. Para 'Presionar "L", si es leyenda, enter para saltar: ', solo dar enter

6. Aparecen instrucciones de como terminar

7. En el shell escribir "(1412-1430) Campesina francesa, líder militar." y dar enter.

8. Seguir escribiendo con "Participó en la guerra de los Cien Años." y dar enter.

9. Escribir "El rey Carlos VII de Valois se coronó gracias a su apoyo", dar enter.

10. Ahora escribir "xxx" y dar enter

11. Aparecen opciones de época. Para 'Epoca (Escribir número): ', teclear '2' y dar enter

12. Aparecen opciones para regiones. Para 'Región (Escribir número): ', teclear '3' y dar enter

13. Vuelve a aparecer el menú del incio. Para 'Opción: ' teclear '1' y dar enter.

14. Para 'Título, sin carácteres especiales, espacios y mayusculas permitidos: ', escribir "Carlo Magno" y dar enter

15. Para 'Presionar "L", si es leyenda, enter para saltar: ', solo dar enter

16. Aparecen instrucciones de como terminar

17. En el shell escribir "(742 - 814). Rey de los francos y lombardos. Primer emperador del Sacro Imperio Romano.", dar enter

18. Escribir "Unificó el imperio con guerras por varias partes del continente.", dar enter

19. Escribir "El imperio fue base para varias de las futuras naciones europeas.", dar enter

20. Escribir "xxx" y dar enter.

21. Aparecen opciones de época. Para 'Epoca (Escribir número): ', teclear '1' y dar enter

22. Aparecen opciones para regiones. Para 'Región (Escribir número): ', teclear '4' y dar enter

23. Vuelve a aparecer el menu del incio. Para "Opción: ", teclear '2', dar enter

24. Ahora se muestra "Texto: Juana de Arco", seguido por la época y región escogida

25. Para "Abrir el documento en modo lectura? Presionar "s" para confirmar, enter para saltar: ", teclear "s"

26. Muestra el texto del archivo para 'juanadearco.txt'

27. Más abajo muestra lo que corresponde a "Texto: Carlo Magno", la época y la región seleccionada

28. Para "Abrir el documento en modo lectura? Presionar "s" para confirmar, enter para saltar: ", teclear "s"

29. Se imprime el texto correpondiente a 'carlomagno.txt'

30. Se vuelve a mostrar el menu de inicio, para "Opción: " Escribir '3'.

31. El programa finaliza


---- Algoritmo por función ----

def tagEpoca():
1. variable 'alta' definida con texto "Edad Media Alta (s.V - s.X)"
2. variable 'baja' definido con texto "Edad Media Baja (s.XI - XV)"
3. se define una lista con variables 'alta' y 'baja'
4. Se imprimen las opciones en forma de lista una por una con un bucle for 'i' en el rango de la lista
5. variable 'opcion' definido con el número que escoja el usuario
6. Al valor de 'variable' se le resta 1 or la naturaleza de los indices en las listas
7. Una variable 'tag' será el item en la lista y la regresa

def tagRegion():
1. Se crean variables por cada región, que equivalen a un texto con el nombre de la región. (Regiones: Norte, Islas británicas, occidente, centro, oriente, sureste, sur)
2. Se crea una lista, que guarda cada una de esas variables
3. Con un bucle for 'i' en el rango de la lista, se va imprimir en forma de lista el texto de cada variable, para dar una opción
4. Se crea variable 'opcion' que recibe un número del usuario
5. Al valor de la variable 'opcion' se le resta 1
6. Se crea variable tag que es el item en la lista en posición del valor de la opcion.

def texto():

1. Se crea una lista vacia representada por variable 'lista'

2. Se presenta variable 'escrita' con ningun valor

3. Se imprimen instrucciones para terminar de escribir ("xxx")

4. Se abre un bucle que corra lo siguiente mientras el escrito no sean las especificadas ("xxx")

5. dentro del bucle, la variable 'escrito' va a ser lo que el usuario escriba antes de un 'enter' (parrafo)

6. Variable 'texto' va a ser 'escrito' pero con un salto de parrafo para que no se imprima todo junto después.

7. Variable 'texto' se añade a la lista creada del principio de la función.

8. El bucle acaba una vez que se escriba "xxx"

9. La función regresa la lista creada (contiene todo el texto)


def crearArchivo(titulo):

1. La función recibe el nombre (tituo) que se le asigna en la función -archivo()-
2. variable 'nombreArchivo' es el título.txt en forma de texto
3. Variable 'archivo' abre el archivo en modo escritura con el nombre en la variable 'nombreArchivo'
4. Variable 'parrafos' se equivale a lo que devuelve la función -texto()- (la lista de texto)
5. El programa escribe las líneas para variable 'archivo'
6. El programa empieza desde el principio en variables 'archivos'.
7. se cierra el archivo
8. La función regresa el archivo -archivo-


def archivo():

1. variable 'nombre' recibe el nombre para el relato que el usuario asigna

2. variable 'veras' recibe entrada de usuario, le pregunta al usuario si es leyenda o no, escribe "L" si lo es, o da 'enter' si no lo es.

3. Variable 'tituloJunto' que recibe el 'nombre' y quita los espacios ' ' los cambia a '' (sin espacio)

4. Al texto de la variable 'tituloJunto' (ya sin espacios), a todas las mayúsculas se convierten en minúsculas. Será nombre propio para el nombre del archivo del relato

5. Se llama la función -crearArchivo(tituloJunto)- usando texto de variable de -tituloJunto-

6. Se crea una lista vacia represantada por la variable 'partes'

7. con variable 'epoca' llama y recibe lo de la función -tagEpoca()-

8. con variable 'region' llama y recibe lo de la función -tagRegion()-

9. Para el primer espacio, 0 de la lista, se le añade 'tituloJunto' (despues servirá para leer el archivo)

10. Para el segundo espacio, 1 de la lista, se le añade 'nombre' (Para mostrar el título del relato después)

11. Para el tercer espacio, 2 de la lista, se le añade 'epoca' (lo imprime después)

12. Para el cuarto espacio, 3 de la lista, se le añade 'region'

13. Recordando la variable 'veras' si era leyenda o no, 'veras' es "l", para el quinto espacio, 4 de la lista, se le añade el texto "Leyenda"

14. la función regresa la lista creada en la variable 'partes'


def iniciar():
  1. Imprime la primera opción de escribir un archivo
  2. Imprime la segunda opción de iniciar librería
  3. Imprime la tercera opción de salir

def lectura(nombre):
1. Definir la variable 'titulo' como el texto del nombre.txt (tituloJunto de antes)
2. Variable 'archivo' abre el archivo usando variable 'titulo' en modo de lectura
3. El programa empieza a leer desde el principio del archivo
4. Variable 'contenido' lee el archivo entero (el texto escrito)
5. Imprimir variable 'contenido'
6. Se cierra el archivo

def main():
1. crea una lista vacia que servirá como librería, la identifica con la variable 'libreria'.
  
2. Mientras continuar sea cierto, toma el siguiente proeceso:
  
3. Se muestran las opciones con la función -iniciar()-
  
4. variable 'opcion' será el número que ponga el usuario basado en el "menu" de iniciar
  
5. Si la opcion es 1, se va a escribir un archivo:\n
6. Con la variable 'historia' se llama la función -archivo()- que va a regresar una lista que guardan datos que se proporcionarán dentro de la función \n
7. La variable 'historia' (lista) se va añadiendo a la matriz de 'libreria'
   
8. Si se escoge la opción 2, se podrán leer los textos:
9. Se abre un bucle for para 'i' en el rango de la matriz 'librería', pasando por cada "historia" guardada
10. Se imprime "Texto: " con el nombre del texto (dato guardado en lista correspondiente dentro de la librería.
11. Se abre otro bucle para 'j' en el rango de la lista detro de la librería (libreria[i]), para los items dentro de la lista correpondiente.
12. Si 'j' es mayor a 1 se imprime cada uno de los items disponibles (libreria[i][j]), no se imprime 'j' = 0 porque es el nombre en mínusculas y sin espacios.
13. Se abre una variable 'decision' que recibe "s" o 'enter' del usuario.
14. Si 'decision' es s, se llama la función -lectura()- con el item en libreria[i][0], que es el nombre corto (se va a usar para abrir el documento en modo de lectura)
