# Démo ZEISS — Proposition de partenariat

Film interactif guidé par clics, avec saisie visible à la souris et vignettes issues du vrai PowerPoint ZEISS.

## Lancer

1. Ouvrir `zeiss_demo.html` dans Chrome ou Edge (fichier autonome, images intégrées)
2. **F** pour le plein écran
3. **Cliquer** (ou Espace) pour avancer aux étapes clés — le remplissage se joue tout seul, lentement, avec le curseur

Démo en ligne : voir le déploiement Vercel du dépôt.

## Parcours

| Pause (clic) | Contenu |
|--------------|---------|
| Intro | Promesse · ~50 slides |
| Après mobile | Saisie terrain (client, enseigne, enjeux, CA, note) |
| Après sync | Cloud · reprise multi-appareil |
| Après bureau | Arguments, axes, podiums, conditions, simulateurs |
| Avant génération | Clic sur « Générer » |
| Après génération | 48 slides · zoom remplissage · IA + notes |
| Fin | PowerPoint uniquement · notification mobile |

## Fichiers

- `zeiss_demo.html` — démo autonome (images base64 intégrées)
- `embed_slides.py` + `slide-data-embed.js` — régénérer l’embed si les PNG changent
- `slides/` — vignettes sources (optionnel en local)
- PPTX source : 115 slides modèle · ~48 retenues dans la démo

## Régénérer les vignettes

Si le PPTX est mis à jour, exporter les slides en PNG (480×270) dans `slides/slide_XXX.png`.
