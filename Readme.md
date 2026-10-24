# WebScraping

Petit projet Python de web scraping réalisé dans le cadre du module Python de L2. Le programme récupère des produits sur Amazon.fr (nom, prix, note, image), les enregistre dans un fichier CSV, puis permet de les consulter et d'en tirer quelques statistiques depuis un menu en console.

> Projet en cours de développement : toutes les fonctionnalités du menu ne sont pas encore terminées (voir la section « État d'avancement »).

## Fonctionnalités

- Scraping d'une page de résultats Amazon.fr avec Selenium
- Nettoyage des prix (suppression du symbole €, conversion en nombre)
- Sauvegarde des produits dans un fichier CSV
- Affichage des données enregistrées
- Statistiques sur les produits : nombre total, prix moyen, produit le moins cher et le plus cher, nombre de produits notés 4 ou plus

## Technologies

- Python 3
- [Selenium](https://www.selenium.dev/) (avec Google Chrome)
- Module `csv` de la bibliothèque standard

## Structure du projet

Le projet suit une organisation de type MVC.

```
WebScraping/
├── app/
│   ├── main.py                     # Point d'entrée du programme
│   ├── controllers/
│   │   └── ControllerScraper.py    # Gère le menu et appelle les bonnes actions
│   ├── views/
│   │   └── ScrapingView.py         # Affichage console (menu, données, statistiques)
│   ├── models/
│   │   ├── Produit.py              # Classe représentant un produit
│   │   └── Depots.py               # Lecture / écriture du CSV et statistiques
│   └── scraper/
│       ├── AmazonScraper.py        # Scraping de la page Amazon avec Selenium
│       └── Parsing.py              # Nettoyage des données (prix)
├── data/
│   └── Technologie/Informatique/
│       └── informatique.csv        # Fichier de sortie du scraping
├── config.py                       # Paramètres (URL, catégorie, chemin du CSV)
└── requirement.txt                 # Dépendances
```

## Installation

1. Cloner ou télécharger le projet, puis se placer dans le dossier :

   ```bash
   cd WebScraping
   ```

2. (Recommandé) Créer un environnement virtuel :

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installer les dépendances :

   ```bash
   pip install -r requirement.txt
   ```

4. Avoir Google Chrome installé. Selenium récupère lui-même le driver correspondant.

## Configuration

Les paramètres se trouvent dans `config.py` :

| Variable | Rôle |
|----------|------|
| `CATEGORIE` | Catégorie affichée dans les statistiques |
| `SOUS_CATEGORIE` | Sous-catégorie affichée dans les statistiques |
| `URL` | Page de résultats Amazon.fr à scraper |
| `CHEMIN` | Chemin du fichier CSV de sortie |

Attention : `CHEMIN` est actuellement un chemin absolu propre à ma machine. Il faut le modifier pour qu'il pointe vers `data/Technologie/Informatique/informatique.csv` sur la vôtre. Le fichier doit déjà exister, sinon la sauvegarde est refusée.

## Utilisation

Depuis la racine du projet :

```bash
python -m app.main
```

Un menu s'affiche dans le terminal :

```
1-Demarrer le scraping
2-Afficher les données scraper
3-Afficher les statistiques
4-Exporter les statistiques
0-Quitter
```

Le fichier CSV produit a la forme suivante :

```
Nom,Prix,Note,Image URL
```

## État d'avancement

- [x] Architecture du projet (modèles, vues, contrôleur, scraper)
- [x] Menu en console
- [x] Nettoyage des prix
- [ ] Scraping Amazon : les sélecteurs CSS restent à finaliser
- [ ] Statistiques : calculs à terminer (prix moyen, note moyenne, min / max)
- [ ] Export des statistiques (option 4 du menu)
- [ ] Gestion des erreurs (produit sans note ou sans prix, page qui ne charge pas)



## Auteur

Diabagate Hassane Ilias, étudiant en L2.