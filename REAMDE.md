# 🚜 WoT Blitz News Scraper

Ce projet est un robot de surveillance automatique pour le jeu **World of Tanks Blitz**. Il parcourt le site officiel, extrait les derniers articles (titres, liens, textes complets, images) et sauvegarde le tout dans un fichier JSON structuré.

## 🌟 Fonctionnalités 
- **Scraping Dynamique** : Utilise Selenium pour simuler un vrai navigateur et contourner les protections JavaScript/SPA du site.
- **Extraction Profonde** : Ne se contente pas des aperçus, il visite chaque page d'article pour extraire le texte complet et les listes d'images.
- **Format JSON** : Sauvegarde les données proprement (UTF-8) pour une intégration facile (Discord Bot, API, Dashboard).
- **Optimisation PowerShell** : Lancement ultra-rapide via la commande personnalisée `go`.

## ⚙️ Fonctionnement technique
Le script suit un processus en "entonnoir" pour garantir la qualité des données :

1. **Phase de Scan** : Ouverture de la page d'accueil `/news/` et détection des balises `.news-list_item`.
2. **Phase de Navigation** : Le robot "clique" sur chaque lien d'article trouvé.
3. **Phase d'Extraction** : Ciblage précis de la zone `.news_content` pour récupérer le texte et les URLs des images.
4. **Phase de Nettoyage** : Suppression des éléments parasites (menus, boutons sociaux, "j h h min min").

## 🛠️ Installation

1. **Cloner le projet** dans un dossier local.
2. **Créer l'environnement virtuel** :
   ```powershell
   python -m venv .venv
