import requests
from bs4 import BeautifulSoup

# URL de la page
url = 'https://quotes.toscrape.com/tableful/'
page = requests.get(url)

# Analyser la page avec BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Chercher toutes les balises <td> qui contiennent les tags
tags_table = soup.find_all("td")

# Vérifier si on a trouvé des tags
if tags_table:
    # Liste pour stocker les tags et leurs occurrences
    tag_list = []

    # Parcourir chaque cellule de la table
    for tag_cell in tags_table:
        # Extraire le texte de la cellule
        tag_text = tag_cell.get_text(strip=True)

        # Séparer les tags et les occurrences
        tag_items = tag_text.split(')')  # Séparer les tags par les parenthèses fermantes

        for item in tag_items:
            if '(' in item:  # Assurer que chaque tag est bien formaté comme 'tag(number)'
                try:
                    tag, count = item.split('(')  # Séparer le tag et son occurrence
                    tag = tag.strip()

                    # Vérifier si le tag commence par "Top Ten tags" collé à un autre mot
                    if "top ten tags" in tag.lower():
                        tag = tag.replace("Top Ten tags", "").strip()  # Supprimer cette partie

                    if tag:  # Vérifier si le tag n'est pas vide après cette opération
                        tag_list.append((tag, int(count)))  # Ajouter à la liste en format (tag, occurrence)
                except ValueError:
                    # S'il y a un problème avec la conversion des nombres, on passe
                    continue

    # Trouver le tag le plus utilisé
    if tag_list:
        most_common_tag = max(tag_list, key=lambda x: x[1])  # Trouver le tag avec l'occurrence maximale

        # Afficher le tag le plus utilisé avec le nombre d'occurrences
        print(f"Le tag le plus utilisé est '{most_common_tag[0]}' avec {most_common_tag[1]} occurrences.")
    else:
        print("Aucun tag pertinent trouvé.")
else:
    print("Aucun tag trouvé sur la page.")
