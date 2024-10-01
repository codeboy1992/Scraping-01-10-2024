import requests
from bs4 import BeautifulSoup

# URL de base pour les citations
base_url = "http://quotes.toscrape.com"
page_number = 1

# Boucle à travers plusieurs pages
while True:
    response = requests.get(f"{base_url}/page/{page_number}/")
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver toutes les citations sur la page
    quotes = soup.find_all('div', class_='quote')

    # Chercher les citations d'Albert Einstein sur la musique
    music_quotes = []
    for quote in quotes:
        author = quote.find('small', class_='author').text  # Récupérer le nom de l'auteur
        text = quote.find('span', class_='text').text
        if author == "Albert Einstein" and ("music" in text.lower() or "musique" in text.lower()):
            music_quotes.append(text)

    # Afficher les citations trouvées
    if music_quotes:
        for quote in music_quotes:
            print(f"Citation sur la musique : {quote}")
        break  # Sortir de la boucle si des citations sont trouvées

    # Passer à la page suivante
    page_number += 1

    # Si on atteint la dernière page, sortir de la boucle
    if page_number > 10:  # Limite le nombre de pages à scrapper
        print("Aucune citation d'Albert Einstein sur la musique trouvée après avoir vérifié plusieurs pages.")
        break
