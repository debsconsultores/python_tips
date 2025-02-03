# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL del pasaje de la Biblia
url = 'https://www.biblegateway.com/'

# Enviar una solicitud GET a la URL
response = requests.get(url)

# Analizar el contenido HTML de la página
soup = BeautifulSoup(response.content, 'html.parser')

title_div = soup.find('span', class_='citation')
verse_text_divs = soup.find('div', id='verse-text')
version = soup.find('div', class_='version-display')

print(f"Versículo: {title_div.text.strip()} - {version.text.strip()}")
print(f"Texto: {verse_text_divs.text.strip()}")

# version = soup.find('div', class_='search-dropdown-display')
# print(version)


# print(version)