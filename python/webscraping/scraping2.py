# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL del pasaje de la Biblia
# url = 'https://www.biblegateway.com/passage/?search=John%208%3A31-32&version=TLA'
url = 'https://www.biblegateway.com/passage/?search=Juan3%3A16&version=TLA'

# Enviar una solicitud GET a la URL
response = requests.get(url)

# Analizar el contenido HTML de la página
soup = BeautifulSoup(response.content, 'html.parser')

title_div = soup.find('div', class_='dropdown-display-text')

verse_text_divs = soup.find('div', class_='passage-text')


print(f"Versículo: {title_div.text.strip()}")
print(f"Texto: {verse_text_divs.text.strip()}")