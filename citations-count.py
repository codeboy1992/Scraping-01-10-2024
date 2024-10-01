import requests

# URL de l'API
api_url = "https://quotes.toscrape.com/api/quotes?page={}"

# variables
page_num = 1
total_quotes = 0
has_quotes = True

while has_quotes:
    # Envoyer une requête à l'API
    response = requests.get(api_url.format(page_num))
    data = response.json()

    # Extraire les citations
    quotes = data.get('quotes', [])

    # Compter le nombre de citations
    total_quotes += len(quotes)

    # Vérifier si d'autres pages existent
    has_quotes = data.get('has_next', False)  # Si 'has_next' est False plus de citations
    page_num += 1

# Afficher le nombre total de citations
print(f"Nombre total de citations : {total_quotes}")
