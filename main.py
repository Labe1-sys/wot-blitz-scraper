from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time

# 1. Config du navigateur
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def extraire_contenu_final(url):
    try:
        driver.get(url)
        time.sleep(4)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        content_area = soup.find('div', class_='news_content')
        
        if content_area:
            # 1. On récupère le texte
            texte = content_area.get_text(separator='\n', strip=True)
            
            # 2. On récupère TOUTES les images de l'article
            images = []
            for img in content_area.find_all('img'):
                src = img.get('src')
                if src:
                    # On s'assure que l'URL est complète
                    img_url = src if src.startswith('http') else "https:" + src
                    images.append(img_url)
            
            return texte, images
        return "Zone non trouvée", []
    except:
        return "Erreur", []

# Dans ta boucle principale, tu modifies ainsi :
# texte_complet, liste_images = extraire_contenu_final(full_link)
# data_finale.append({
#     "titre": titre,
#     "url": full_link,
#     "contenu_detaille": texte_complet,
#     "images": liste_images
# })

try:
    print("🚀 Démarrage du scan...")
    driver.get("https://eu.wotblitz.com/fr/news/")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    base_url = "https://eu.wotblitz.com"
    data_finale = []

    # On récupère les liens dans news-list_item (image_48f43d.png)
    articles = soup.find_all('div', class_='news-list_item')

    for art in articles[:3]: # On teste sur les 3 premiers
        link_tag = art.find('a', class_='news-annotation_link')
        
        if link_tag:
            href = link_tag.get('href')
            full_link = base_url + href
            
            # Récupération du titre de l'aperçu
            title_tag = art.find('div', class_='news-annotation_title')
            titre = title_tag.get_text(strip=True) if title_tag else "News"
            
            print(f"📖 Lecture de : {titre}")
            
            # On entre dans l'article
            texte_complet = extraire_contenu_final(full_link)
            
            data_finale.append({
                "titre": titre,
                "url": full_link,
                "contenu_detaille": texte_complet
            })

    # Sauvegarde
    with open('actu_blitz_complet.json', 'w', encoding='utf-8') as f:
        json.dump(data_finale, f, indent=4, ensure_ascii=False)

    print("\n✅ Terminé ! Ton fichier 'actu_blitz_complet.json' est prêt.")

finally:
    driver.quit()