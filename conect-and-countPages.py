import requests
from bs4 import BeautifulSoup

# URL du site et de la page de login
login_url = "https://quotes.toscrape.com/login"
session = requests.Session()

# Récupérer la page de login
response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraire le token CSRF (s'il y en a un)
csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")

# Définir les informations de login
login_data = {
    "csrf_token": csrf_token,  # Token CSRF (important si présent)
    "username": "yourusername",  # Remplace par un nom d'utilisateur
    "password": "yourpassword"  # Remplace par un mot de passe
}

# Envoyer une requête POST avec les informations de connexion
response = session.post(login_url, data=login_data)

# Vérifier si la connexion a réussi
quotes_page = session.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(quotes_page.text, "html.parser")

# Vérifier si on est connecté
if soup.find("a", string="Logout"):
    print("Connexion réussie !")
else:
    print("Échec de la connexion.")

# Extraire et afficher quelques citations
quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.get_text())
# calculer le nombre de citations

page_num = 1
has_next = True

while has_next:
    # Accéder à la page
    page_url = f"https://quotes.toscrape.com/page/{page_num}/"
    response = session.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Vérifier s'il y a un lien "Next"
    next_button = soup.find("li", class_="next")

    if next_button:
        page_num += 1  # Passer à la page suivante si "Next" est trouvé
    else:
        has_next = False  # Pas de lien "Next", on est à la dernière page
print()
print(f"Nombre total de pages : {page_num}")
