import requests

def obtener_contenido(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si hubo algún error en la solicitud
        return respuesta.text
    except requests.exceptions.HTTPError as err:
        print(f"Error HTTP: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    contenido = obtener_contenido(url)
    if contenido:
        print(contenido)
