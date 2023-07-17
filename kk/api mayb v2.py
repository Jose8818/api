import requests
import geocoder
from googletrans import Translator

API_KEY = "f19785cdf4aa95bad40e82b101657628"


def obtener_clima(latitud, longitud):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    datos_clima = response.json()

    if response.status_code == 200:
        temperatura = datos_clima["main"]["temp"]
        descripcion = datos_clima["weather"][0]["description"]
        return temperatura, descripcion
    else:
        return None


def traducir_texto(texto, destino):
    translator = Translator()
    translation = translator.translate(texto, dest=destino)
    return translation.text


def mostrar_clima(latitud, longitud, idioma_destino):
    clima = obtener_clima(latitud, longitud)

    if clima is not None:
        temperatura, descripcion = clima

        descripcion_traducida = traducir_texto(descripcion, idioma_destino)

        print(f"El clima en tu ubicación actual es: {descripcion_traducida}")
        print(f"La temperatura actual es: {temperatura}°C")

        if temperatura > 30:
            print("¡Advertencia! La temperatura es mayor a 30 grados.")
        elif temperatura < 5:
            print("¡Advertencia! La temperatura es menor a 5 grados.")
    else:
        print("No se pudo obtener el clima para la ubicación actual.")


g = geocoder.ip('me')
latitud, longitud = g.latlng

idioma_destino = "es"

mostrar_clima(latitud, longitud, idioma_destino)
