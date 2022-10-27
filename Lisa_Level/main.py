from email.quoprimime import quote
from requests.models import Response
import requests
import json
import threading
import time
import csv
import shutil
import os
import string

# definimos la función que cuenta las veces que aparece cada palabra
def word_count(frase, contar):
  counts = contar
  words = frase.split() # separamos las palabras, después de un espacio cuenta una palabra nueva

  for i in words:
    if i in counts: 
      counts[i] += 1
    else:
      counts[i] = 1
  return counts

contar = {}
# obtenemos los datos de la API
while True: 
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    response = requests.get(URL)
    datos = response.json()
    quote = datos[0]["quote"]
    character = datos[0]["character"]
    image = datos[0]["image"]
    print(f"El personaje {character} ha dicho: {quote}")

# creamos un nuevo directorio para cada personaje 
# utilizamos la condición if not para eliminar el error que se producía al salir un personaje ya existente
    if not os.path.isdir("Lisa_Level/"+character+"/"):
      os.mkdir("Lisa_Level/"+character+"/")

# añadimos cada imagen a su carpeta correspondiente
    img_data = requests.get(image).content
    with open(f'Lisa_Level/{character}/{character}.png', 'wb') as handler:
      handler.write(img_data)

# creamos el csv de cada personaje en su carpeta correspondiente
    data = [datos[0]["character"], datos[0]["quote"]]
    with open(f'Lisa_Level/{character}/{character}.csv', 'a') as file:
      writer = csv.writer(file)
      writer.writerow(data)

# eliminamos los signos de puntuación de las frases
# utilizamos todos los simbolos del método maketrans() excepto ' ya que en inglés es muy usado para contraer palabras y daría lugar a errores en el contador
    simbolos = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    new_frase = quote.translate(str.maketrans('', '', simbolos))
    contar = word_count(new_frase, contar)

# creamos un archivo .csv para guardar el conteo de palabras
    with open('Lisa_Level/Contador.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in contar.items():
          writer.writerow([key, value])

    time.sleep(30)

