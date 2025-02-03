import time
from googletrans import Translator

felicitaciones = [
    "Feliz Año Nuevo (Español)",
    "Happy New Year (Inglés)",
    "Bonne Année (Francés)",
    "Feliz ano novo (Portugués)",
    "سال نو مبارک (Persa)",
    "שנה טובה (Hebreo)"
]

for felicitar in felicitaciones:
    print(felicitar)
    time.sleep(1)

# Inicializa el traductor
translator = Translator()

# Lista de idiomas a los que quieres traducir
# idiomas = ['es', 'en', 'fr', 'pt', 'fa', 'he','de','it','ja','ru']
idiomas = ['de','it','ja','ru','ar','ko','zh-cn']

# Texto a traducir
texto = "Feliz Año Nuevo"

print("*********")
# Traduce y muestra las felicitaciones en diferentes idiomas
for idioma in idiomas:
    traduccion = translator.translate(texto, dest=idioma)
    print(f"{traduccion.text} ({traduccion.dest})")
    time.sleep(1)

print("🎄💥 Vamos a Celebrar🎄💥")
