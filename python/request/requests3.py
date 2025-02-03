import requests
import json

# Definir la URL de la API
url = "https://jsonplaceholder.typicode.com/posts/1"

# Realizar la solicitud GET
respuesta = requests.get(url)

# Verificar el estado de la respuesta
if respuesta.status_code == 200:
    # Mostrar el contenido de la respuesta
    print("Datos obtenidos:")
    # print(respuesta.json())
    print(json.dumps(respuesta.json(), indent=4, sort_keys=True))
else:
    print(f"Error en la solicitud: {respuesta.status_code}")
