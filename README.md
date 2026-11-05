# Papeterie Marylee

Site vitrine statique (HTML, CSS, JavaScript) reprenant la mise en page du
site Squarespace d'origine, sans la partie boutique en ligne.

## Contenu

```
index.html            Accueil
contact.html          Contact
projets/*.html        Une page par projet du portfolio
css/style.css         Toute la mise en forme (couleurs et polices en haut du fichier)
js/main.js            En-tête fixe et menu mobile
tools/download_images.py  Rapatrie les images de Squarespace dans images/
```

## Mise en ligne sur GitHub Pages

1. Créez un dépôt sur GitHub et téléversez tout le contenu de ce dossier.
2. Dans le dépôt : **Settings → Pages → Build and deployment**,
   choisissez *Deploy from a branch*, branche `main`, dossier `/ (root)`.
3. Le site sera publié à `https://votre-nom.github.io/nom-du-depot/`.
4. Pour garder `papeteriemarylee.com`, ajoutez le domaine dans
   **Settings → Pages → Custom domain**, puis suivez les instructions DNS de GitHub.

## Avant de quitter Squarespace

Les images sont encore hébergées chez Squarespace. Lancez une fois, sur votre ordinateur :

```
python3 tools/download_images.py
```

Le script télécharge chaque image dans `images/` et met les liens à jour.

## Personnaliser

- **Couleurs** : les 5 couleurs de la palette sont au début de `css/style.css`.
- **Polices** : Shippori Mincho est identique à l'original. orpheus-pro et
  adobe-garamond-pro sont des polices Adobe Fonts ; elles sont remplacées par
  Cormorant et EB Garamond. Avec un abonnement Adobe Fonts, collez le lien de
  votre kit dans le `<head>` de chaque page pour retrouver les originales.
- **Lien de la boutique** : cherchez `papeteriemarylee.com/boutique` et
  remplacez-le par l'adresse de votre nouvelle boutique.
- **Projets** : ajoutez les images de chaque projet dans `projets/nom-du-projet.html`.
