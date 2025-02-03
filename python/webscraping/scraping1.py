# pip install requests
# pip install beautifulsoup4
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL del pasaje de la Biblia
url = 'https://www.biblegateway.com/passage/?search=John%208%3A31-32&version=TLA'

# Enviar una solicitud GET a la URL
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar el div con id 'passage-box'
    passage_box = soup.find('div', class_='passage-col')

    if passage_box:
        # Extraer el título y el texto
        title_div = passage_box.find('div', class_='dropdown-display-text')
        verse_text_divs = passage_box.find_all('div', class_='passage-text')

        if title_div and verse_text_divs:
            title = title_div.text.strip()
            verse_texts = [verse.text.strip().replace('Read full chapter', '').strip() for verse in verse_text_divs]

            # Imprimir el título y el texto extraídos
            print(f"Title: {title}")
            for i, verse_text in enumerate(verse_texts, start=1):
                print(f"Verse {i}: {verse_text}")
        else:
            print("No se encontraron los elementos 'dropdown-display-text' o 'passage-text'.")
    else:
        print("No se encontró el elemento 'passage-box'.")
else:
    print(f"Error al acceder a la página: {response.status_code}")


