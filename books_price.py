import requests
from bs4 import BeautifulSoup

base_url = 'https://books.toscrape.com/'

# Récupérer la page d'accueil et analyser le contenu
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver toutes les catégories de livres
categories = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')

for category in categories:
    category_name = category.get_text().strip()
    category_url = base_url + category.find('a')['href']

    # Scrapper chaque catégorie
    response_category = requests.get(category_url)
    soup_category = BeautifulSoup(response_category.text, 'html.parser')

    books = soup_category.find_all('article', class_='product_pod')
    total_price = 0
    book_count = 0

    for book in books:
        price = book.find('p', class_='price_color').text.strip()
        price = price.replace('Â£', '').replace('£', '')  # Enlève le symbole de la monnaie
        total_price += float(price)
        book_count += 1

    average_price = total_price / book_count if book_count > 0 else 0
    print(f"Catégorie: {category_name}, Nombre de livres: {book_count}, Prix moyen: £{average_price:.2f}")
