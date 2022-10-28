## ENTREGABLE 0: THE SIMPSONS
#
![THE_SIMPSONS](https://upload.wikimedia.org/wikipedia/commons/9/98/The_Simpsons_yellow_logo.svg)

### Maggie Level (obligatorio)

1. Usando google colab crear un notebook que consuma la api de los simpsons y haga una
consulta cada 30seg a la API
2. El código debe guardar cada quote en un csv dentro de una carpeta con el nombre del
personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos).
3. Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de
manera autónoma. El Docker debe tener el código en una carpeta app.
4. El fichero docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger
citas de ellos dos.

### Lisa Level (obligatorio)

1. Mejorad el código para descargar la imagen del personaje y guardadla en la carpeta del
mismo.
2. El código debe mantener un diccionario de palabras y escribir en cada iteración en un
fichero el conteo de palabras que lleva.
a. The;1
b. Great;2
3. El código debe crear de manera dinámica las carpetas con nuevos personajes

### Bart Level (opcional)

1. Construid un Docker-compose con una imagen de un contenedor de Jupyter.
2. Dentro del Jupyter generad un notebook con una gráfica mostrando las
palabras más habituales en las quotes
3. Mostrar un listado de las carpetas y las fotos de los personajes en el jupyter
4. Docker-compose debe ser capaz de hacer build del contenedor original