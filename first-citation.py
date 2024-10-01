from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Chemin vers ton chromedriver (remplace par le chemin correct)
chromedriver_path = r"C:\Program Files (x86)\chromedriver.exe"

# Créer un objet Service avec le chemin vers ChromeDriver
service = Service(executable_path=chromedriver_path)

# Initialisation de Selenium avec le service ChromeDriver
driver = webdriver.Chrome(service=service)

# Ouvrir la page avec Selenium
url = 'https://quotes.toscrape.com/js/page/10/'
driver.get(url)

# Attendre que la page se charge (augmente si la page est lente)
time.sleep(3)

# Extraire le contenu de la page avec BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Trouver la première citation en utilisant la classe 'quote'
first_quote = soup.find("div", class_="quote")

if first_quote:
    # Extraire le texte de la citation
    text = first_quote.find("span", class_="text").get_text()
    # Extraire le nom de l'auteur
    author = first_quote.find("small", class_="author").get_text()

    # Stocker la première citation dans une variable
    stored_quote = {
        "text": text,
        "author": author
    }

    print(f"Citation: {stored_quote['text']}")
    print(f"Auteur: {stored_quote['author']}")
else:
    print("Aucune citation trouvée.")

# Fermer le navigateur après avoir fini
driver.quit()
