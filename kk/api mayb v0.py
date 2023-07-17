import requests

API_KEY = "f19785cdf4aa95bad40e82b101657628"


def obtener_clima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    datos_clima = response.json()

    if response.status_code == 200:
        temperatura = datos_clima["main"]["temp"]
        descripcion = datos_clima["weather"][0]["description"]
        return temperatura, descripcion
    else:
        return None


def mostrar_clima(ciudad):
    clima = obtener_clima(ciudad)

    if clima is not None:
        temperatura, descripcion = clima
        print(f"El clima en {ciudad} es: {descripcion}")
        print(f"La temperatura actual es: {temperatura}°C")

        if temperatura > 30:
            print("¡Advertencia! La temperatura es mayor a 30 grados.")
        elif temperatura < 5:
            print("¡Advertencia! La temperatura es menor a 5 grados.")
    else:
        print("No se pudo obtener el clima para la ubicación especificada.")


ciudad = input("Ingresa tu ubicación (ciudad): ")
mostrar_clima(ciudad)
