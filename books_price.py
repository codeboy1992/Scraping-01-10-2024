import requests
from bs4 import BeautifulSoup
import re  # Importer le module re pour les expressions régulières

base_url = 'https://books.toscrape.com/'

# Récupérer la page d'accueil et analyser le contenu
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver toutes les catégories de livres
categories = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')

total_categories = len(categories)  # Nombre total de catégories

for category in categories:
    category_name = category.get_text().strip()
    category_url = base_url + category.find('a')['href']

    # Accéder à la page de la catégorie pour obtenir le nombre total de livres
    response_category = requests.get(category_url)
    soup_category = BeautifulSoup(response_category.text, 'html.parser')

    # Trouver le nombre total de livres dans la catégorie
    results_info = soup_category.find('form', class_='form-horizontal')
    expected_books = int(results_info.find_all('strong')[0].get_text()) if results_info else 0

    # Initialiser les variables pour chaque catégorie
    total_price = 0
    book_count = 0
    current_page_url = category_url  # Démarrer à la première page

    while current_page_url:
        # Scrapper chaque page de la catégorie
        response_category = requests.get(current_page_url)
        soup_category = BeautifulSoup(response_category.text, 'html.parser')

        # Trouver tous les livres sur la page
        books = soup_category.find_all('article', class_='product_pod')

        # Compter les livres et les prix
        for book in books:
            price = book.find('p', class_='price_color').text.strip()
            price = price.replace('Â£', '').replace('£', '').replace(',', '')  # Enlève le symbole de la monnaie
            total_price += float(price)
            book_count += 1

        # Vérifier s'il y a une page suivante
        next_button = soup_category.find('li', class_='next')
        if next_button:
            next_page_url = next_button.find('a')['href']
            current_page_url = category_url.rsplit('/', 1)[
                                   0] + '/' + next_page_url  # Construire l'URL de la page suivante
        else:
            current_page_url = None  # Pas de page suivante

    average_price = total_price / book_count if book_count > 0 else 0
    print(
        f"Catégorie: {category_name}, Livres attendus: {expected_books}, Livres scrappés: {book_count}, Prix moyen: £{average_price:.2f}")

# Afficher le nombre total de catégories
print(f"\nNombre total de catégories: {total_categories}")
