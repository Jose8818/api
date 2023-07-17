import requests
from flask import Flask, render_template, request
import geocoder
from googletrans import Translator
import random

app = Flask(__name__)

API_KEY = "f19785cdf4aa95bad40e82b101657628"

def obtener_clima(latitud, longitud):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    datos_clima = response.json()

    if response.status_code == 200:
        clima = {
            "temperatura": datos_clima["main"]["temp"],
            "descripcion": datos_clima["weather"][0]["description"],
            "humedad": datos_clima["main"]["humidity"],
        }
        return clima
    else:
        return None

def traducir_texto(texto, destino):
    translator = Translator()
    translation = translator.translate(texto, dest=destino)
    return translation.text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ciudad = request.form['ciudad']

        g = geocoder.osm(ciudad)
        latitud, longitud = g.latlng

        idioma_destino = "es"

        clima = obtener_clima(latitud, longitud)
        if clima is not None:
            clima_traducido = {}
            for clave, valor in clima.items():
                if isinstance(valor, str):
                    clima_traducido[clave] = traducir_texto(valor, idioma_destino)
                else:
                    clima_traducido[clave] = valor

            return render_template('clima.html', ciudad=ciudad, **clima_traducido)
        else:
            error = "No se pudo obtener el clima para la ubicación especificada."
            return render_template('error.html', error=error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
