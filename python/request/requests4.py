import requests
import json

# Definir la URL de la API
usuario = "octocat"
url = f"https://api.github.com/users/{usuario}"

# Realizar la solicitud GET
respuesta = requests.get(url)

# Verificar el estado de la respuesta
if respuesta.status_code == 200:
    # Convertir la respuesta a JSON
    datos = respuesta.json()
    
    # Formatear y mostrar los datos
    print("Datos del usuario obtenidos:")
    print(json.dumps(datos, indent=4, sort_keys=True))
else:
    print(f"Error en la solicitud: {respuesta.status_code}")
