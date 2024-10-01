import requests
from bs4 import BeautifulSoup

# URL de la page aléatoire
url = "https://quotes.toscrape.com/random"
unique_quotes = {}  # Dictionnaire pour les citations uniques
duplicate_quotes = {}  # Dictionnaire pour les doublons
target_quotes = 100  # Nombre de citations distinctes à récupérer

# Fonction pour scrapper une citation
def scrape_quote():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Récupérer la citation
    quote_text = soup.find('span', class_='text').text
    author = soup.find('small', class_='author').text
    tags = [tag.text for tag in soup.find_all('a', class_='tag')]

    return {
        'quote': quote_text,
        'author': author,
        'tags': tags
    }

# Boucle pour récupérer des citations jusqu'à 100 uniques
while len(unique_quotes) < target_quotes:
    new_quote = scrape_quote()
    quote_identifier = (new_quote['quote'], new_quote['author'])  # Identifier unique

    if quote_identifier not in unique_quotes:
        unique_quotes[quote_identifier] = new_quote  # Ajouter à unique
        print(f"Unique Quote {len(unique_quotes)}: {new_quote['quote']}\nAuthor: {new_quote['author']}\nTags: {', '.join(new_quote['tags'])}\n")
    else:
        # Ajouter au dictionnaire des doublons
        if quote_identifier not in duplicate_quotes:
            duplicate_quotes[quote_identifier] = new_quote
        print(f"Duplicate found: {new_quote['quote']}\nAuthor: {new_quote['author']}\nTags: {', '.join(new_quote['tags'])}\n")

# Afficher les résultats
print(f"\nTotal des citations uniques récupérées : {len(unique_quotes)}")
print(f"Total des doublons trouvés : {len(duplicate_quotes)}")
