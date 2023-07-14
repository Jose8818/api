import requests
import geocoder

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


def mostrar_clima(latitud, longitud):
    clima = obtener_clima(latitud, longitud)

    if clima is not None:
        temperatura, descripcion = clima
        print(f"El clima en tu ubicación actual es: {descripcion}")
        print(f"La temperatura actual es: {temperatura}°C")

        if temperatura > 30:
            print("¡Advertencia! La temperatura es muy alta, recomendamos que se mantenga en casa y no salga a menos que sea necesario. ¡Mantengase hidratado!")
        elif temperatura < 5:
            print("¡Advertencia! La temperatura es muy baja. ¡briguese bien!")
    else:
        print("No se pudo obtener el clima para la ubicación actual.")


# Obtener la ubicación actual
g = geocoder.ip('me')
latitud, longitud = g.latlng

# Mostrar el clima de la ubicación actual
mostrar_clima(latitud, longitud)
