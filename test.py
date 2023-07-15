import app
import geocoder

def test():
    ciudad = "Apodaca"
    g = geocoder.osm(ciudad)
    latitud, longitud = g.latlng

    resultado = app.obtener_clima(latitud, longitud)

    if resultado is None:
        print("Error: El resultado es nulo")
    else:
        print("La temperatura en Apodaca es:", resultado)

test()
