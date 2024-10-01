import requests
from bs4 import BeautifulSoup
from collections import Counter

# URL de la page à scraper
url = "https://quotes.toscrape.com/tableful/"

# Envoyer une requête GET à la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Liste pour stocker les tags
tags_list = []

# Trouver tous les <td>
tds = soup.find_all('td')

for td in tds:
    # Ignorer les <td> avec un attribut rowspan
    if td.has_attr('rowspan'):
        continue

    # Vérifie si le <td> contient le mot "Tags:"
    if "Tags:" in td.text:
        # Extraire les tags à l'intérieur du <td>
        tags = td.find_all('a')  # Cherche tous les <a> dans le <td>
        for tag in tags:
            tags_list.append(tag.text.strip())  # Ajouter chaque tag à la liste

# Afficher tous les tags extraits pour vérification
print("Tags extraits:", tags_list)

# Compter la fréquence des tags
tags_count = Counter(tags_list)

# Obtenir le top 3 des tags
top_tags = tags_count.most_common(3)

# Afficher le résultat
print("Top 3 des tags:")
for tag, count in top_tags:
    print(f"{tag}: {count}")
