import requests
from bs4 import BeautifulSoup
import json

def buscarRut():
    
    rut = input("ingresa un rut ej 8947220-2: ")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://rutificador.net/rut/',
    }

    data = {
        'rut': f'{rut}',
    }

    response = requests.post('https://rutificador.net/wp-search/rut.php', headers=headers, data=data)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'tabla-resultados'})

    for datos in (table.findAll('tr')[1:]):
        rut = datos.findAll('td')[0].text
        nombre = datos.findAll('td')[1].text
        edadAprox = datos.findAll('td')[2].text
        sexo = datos.findAll('td')[3].text
        domicilio = datos.findAll('td')[4].text
        ciudad = datos.findAll('td')[5].text

    fila = {
        "rut": rut,
        "nombre": nombre,
        "edadAprox": edadAprox,
        "sexo": sexo,
        "domicilio": domicilio,
        "ciudad": ciudad
    }

    patch = f"{rut}.json"

    archive = open(patch, "w", encoding="utf-8")
    json.dump(fila, archive, ensure_ascii=False, indent=4)

    print(f"datos de {rut} guardados exitosamente")

def buscarName():

    name = input("Ingresa un nombre completo ej BASTIAN JOSHUA REYES REYES: ").upper()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://rutificador.net/',
    }

    data = {
        'nombre': f'{name}',
    }

    response = requests.post('https://rutificador.net/wp-search/nombre.php', headers=headers, data=data)

    jotason = response.json()

    html = jotason.get("html")
    
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'id': 'tabla-resultados'})

    for datos in (table.findAll('tr')[1:]):
        rut = datos.findAll('td')[0].text
        nombre = datos.findAll('td')[1].text
        sexo = datos.findAll('td')[2].text
        domicilio = datos.findAll('td')[3].text
        ciudad = datos.findAll('td')[4].text
        
    fila = {
        
        "rut": rut,
        "nombre": nombre,
        "sexo": sexo,
        "domicilio": domicilio,
        "ciudad": ciudad
    }
   
    patch = f"{nombre}.json"

    archive = open(patch, "w", encoding="utf-8")
    json.dump(fila, archive, ensure_ascii=False, indent=4)

    print(f"datos de {nombre} guardados exitosamente")
     
print("1. Buscar por nombre")
print("1. Buscar por rut")

menu = input("Escoge una opcion: ")

if menu == "1":
 buscarName()

elif menu == "2":
  buscarRut()

else: print("opcion invalida")