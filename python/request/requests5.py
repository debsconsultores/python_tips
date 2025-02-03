import requests
import json

# Definir la URL de la API
url = "https://jsonplaceholder.typicode.com/posts/1"

# Realizar la solicitud GET
respuesta = requests.get(url)

# Verificar el estado de la respuesta
if respuesta.status_code == 200:
    # Convertir la respuesta a JSON
    datos = respuesta.json()
    
    # Inicializar variables con los valores de retorno
    user_id = datos['userId']
    post_id = datos['id']
    titulo = datos['title']
    cuerpo = datos['body']
    
    # Formatear y mostrar los datos
    print("Datos del post obtenidos:")
    print(f"User ID: {user_id}")
    print(f"Post ID: {post_id}")
    print(f"Título: {titulo}")
    print(f"Cuerpo: {cuerpo}")
else:
    print(f"Error en la solicitud: {respuesta.status_code}")
