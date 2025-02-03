import requests

# Definir la URL
url = "https://jsonplaceholder.typicode.com/posts"

# Realizar la solicitud GET
respuesta = requests.get(url)

# Verificar el estado de la respuesta
if respuesta.status_code == 200:
    print("Solicitud exitosa!")
else:
    print(f"Error en la solicitud: {respuesta.status_code}")

# Mostrar el contenido de la respuesta
# print(respuesta.text)
