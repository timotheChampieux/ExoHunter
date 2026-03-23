# 📖 Glossaire Technique et Scientifique - Projet ExoHunter

Ce document définit les termes clés utilisés dans le pipeline de détection d'exoplanètes par la méthode des transits. Il est destiné à faciliter la compréhension du projet pour tout chercheur ou ingénieur, quel que soit son domaine d'expertise initial.

---

# 🌌 Astrophysique

## BJD (Barycentric Julian Date)
**Définition :**  
Le jour julien corrigé pour le centre de masse du système solaire (le barycentre). Contrairement au temps terrestre, il supprime les variations de temps de parcours de la lumière dues au mouvement de la Terre autour du Soleil.  
**Contexte dans le projet :**  
Unité de temps standard utilisée dans l'axe `time` des objets `LightCurve`.

## Binaire à éclipses
**Définition :**  
Système de deux étoiles orbitant l'une autour de l'autre. Si leur plan orbital est aligné avec notre ligne de visée, elles s'éclipsent mutuellement, créant une chute de luminosité périodique.  
**Contexte dans le projet :**  
C'est le principal "faux positif" (imposteur) qui peut être confondu avec une planète géante.  
**Alias :** EB, Eclipsing Binary.

## Courbe de lumière
**Définition :**  
Série temporelle de la luminosité (flux) d'un objet céleste mesurée sur une période donnée.  
**Contexte dans le projet :**  
La donnée d'entrée brute traitée par le pipeline pour y chercher des motifs.  
**Alias :** Light Curve, LC.

## Durée de transit
**Définition :**  
Le temps (généralement en heures ou jours) que met une planète pour passer devant son étoile.  
**Contexte dans le projet :**  
Paramètre extrait par l'algorithme BLS pour caractériser la taille de l'orbite.

## Époque (T0)
**Définition :**  
Le moment précis du centre du premier transit observé dans les données.  
**Contexte dans le projet :**  
Utilisé comme point de référence pour replier la courbe de lumière en phase.  
**Alias :** Transit Time, Centre du transit.

## Exoplanète
**Définition :**  
Planète située en dehors de notre système solaire, orbitant autour d'une autre étoile.  
**Contexte dans le projet :**  
L'objet de la recherche finale.

## Flux
**Définition :**  
Quantité d'énergie lumineuse reçue par unité de surface et de temps.  
**Contexte dans le projet :**  
La valeur mesurée (axe Y) dans les courbes de lumière.

## Ingress / Egress
**Définition :**  
L'Ingress est la phase d'entrée de la planète devant le disque stellaire (chute du flux). L'Egress est la phase de sortie (remontée du flux).  
**Contexte dans le projet :**  
Ces phases sont critiques pour le calcul de la forme du transit ; le pipeline utilise des marges (`mask_width`) pour s'assurer de bien les couvrir.

## Missions (Kepler, TESS, K2)
**Définition :**  
Télescopes spatiaux dédiés à la photométrie de précision. Kepler (et sa mission étendue K2) a révolutionné le domaine. TESS (Transiting Exoplanet Survey Satellite) scanne actuellement tout le ciel.  
**Contexte dans le projet :**  
Les sources de données ingérées par le module `loader.py`.

## Période orbitale
**Définition :**  
Le temps nécessaire à une planète pour effectuer une révolution complète autour de son étoile.  
**Contexte dans le projet :**  
Paramètre principal détecté par le périodogramme BLS.

## Profondeur de transit
**Définition :**  
La fraction de lumière bloquée par la planète. Elle est directement proportionnelle au rapport des surfaces : $\delta \approx (R_{planète} / R_{étoile})^2$.  
**Contexte dans le projet :**  
Utilisée dans `metrics.py` pour déduire le rayon de la planète.  
**Alias :** Depth, Transit Depth.

## Rayon stellaire (Rs)
**Définition :**  
La taille physique de l'étoile hôte, généralement exprimée en rayons solaires ($R_{\odot}$).  
**Contexte dans le projet :**  
Paramètre d'entrée indispensable pour convertir la profondeur de transit en taille réelle (km) de la planète.

## Transit astronomique
**Définition :**  
Événement où un corps céleste passe entre un observateur et une source lumineuse, occultant une partie de cette source.  
**Contexte dans le projet :**  
La signature physique recherchée par le pipeline (le "signal").

---

# 📈 Traitement du Signal et Statistiques

## Alias / Harmoniques
**Définition :**  
Signaux apparaissant à des multiples ou des fractions de la fréquence réelle (ex: détecter un signal à 10 jours alors que la planète orbite en 5 jours).  
**Contexte dans le projet :**  
Le pipeline inclut un filtre pour rejeter ces détections redondantes.

## BLS (Box Least Squares)
**Définition :**  
Algorithme de détection de signaux périodiques qui modélise le transit comme une boîte rectangulaire périodique.  
**Contexte dans le projet :**  
L'outil mathématique central (`to_periodogram`) utilisé pour scanner les fréquences.

## Detrending
**Définition :**  
Processus de retrait des tendances à long terme d'une série temporelle pour stabiliser la ligne de base.  
**Contexte dans le projet :**  
Effectué par la fonction `flatten` pour isoler les transits des variations stellaires lentes.  
**Alias :** Retrait de tendance.

## Masquage de transit
**Définition :**  
Action de supprimer les points de données appartenant à un transit déjà identifié.  
**Contexte dans le projet :**  
Permet de "nettoyer" la courbe pour chercher d'autres planètes plus petites cachées dans le signal.

## Normalisation
**Définition :**  
Action de diviser le flux par sa valeur médiane pour que la luminosité de base de l'étoile soit égale à 1.0.  
**Contexte dans le projet :**  
Facilite la comparaison entre différentes étoiles et le calcul de la profondeur en pourcentage.

## Odd/Even Depth Ratio
**Définition :**  
Comparaison de la profondeur des transits pairs et impairs.  
**Contexte dans le projet :**  
Test de validation : si le ratio s'éloigne de 1.0, le signal est probablement une binaire à éclipses (deux étoiles de tailles différentes) plutôt qu'une planète.

## Outliers
**Définition :**  
Points de données aberrants causés par des erreurs instrumentales ou des rayons cosmiques.  
**Contexte dans le projet :**  
Supprimés via `remove_outliers` (Sigma-clipping).

## Périodogramme
**Définition :**  
Graphique montrant la puissance d'un signal en fonction de la fréquence (ou de la période).  
**Contexte dans le projet :**  
Résultat visuel du scan BLS où les pics indiquent les périodes probables.

## Phase / Repliement de phase
**Définition :**  
Action de superposer tous les cycles orbitaux sur une seule période (de 0 à 1 ou -0.5 à 0.5).  
**Contexte dans le projet :**  
Permet de "moyenner" le bruit et de voir clairement la forme du transit.  
**Alias :** Phase folding.

## ppm (parts per million)
**Définition :**  
Unité de mesure de profondeur. $10\,000$ ppm = $1\%$.  
**Contexte dans le projet :**  
Utilisé pour exprimer la profondeur des transits (un transit de la Terre devant le Soleil est de ~100 ppm).

## Savitzky-Golay
**Définition :**  
Type de filtre numérique utilisé pour lisser les données en ajustant des polynômes locaux.  
**Contexte dans le projet :**  
Algorithme utilisé par `flatten` pour le detrending.

## SNR (Signal-to-Noise Ratio)
**Définition :**  
Rapport entre l'amplitude du signal (le transit) et l'écart-type du bruit.  
**Contexte dans le projet :**  
Principal critère de détection. Un SNR > 7.1 est généralement requis pour une détection statistique robuste.  
**Alias :** Rapport Signal sur Bruit.

---

# 💻 Informatique et Bibliothèques

## Astropy
**Définition :**  
Bibliothèque Python fondamentale pour l'astronomie (gestion des unités, des coordonnées, du temps).  
**Contexte dans le projet :**  
Utilisée par Lightkurve pour la gestion rigoureuse des structures de données.

## Lightkurve
**Définition :**  
Bibliothèque spécialisée pour l'analyse des courbes de lumière des missions Kepler et TESS.  
**Contexte dans le projet :**  
Cœur technologique du projet (objets `LightCurve`, `Periodogram`).

## NumPy
**Définition :**  
Bibliothèque de calcul numérique pour Python.  
**Contexte dans le projet :**  
Utilisée pour les manipulations de bas niveau (tableaux, masques, médianes).

## Stitching
**Définition :**  
Action de "recoudre" ensemble plusieurs segments de courbes de lumière (Quarters ou Sectors) pour obtenir une série continue.  
**Contexte dans le projet :**  
Géré dans `loader.py` via `stitch()`.

---

# 🚀 Annexes : Concepts Approfondis

## Le dilemme du window_length (Lissage)
**Définition :**  
Compromis critique lors du detrending. Une fenêtre de lissage trop petite risque de considérer le transit comme une variation stellaire et de le supprimer (underfitting). Une fenêtre trop large ne corrigera pas assez le bruit basse fréquence.  
**Contexte dans le projet :**  
Paramètre configurable dans le module Expert.

## L'impact de la cadence
**Définition :**  
Fréquence à laquelle le télescope prend une mesure (ex: toutes les 2 min ou toutes les 30 min).  
**Contexte dans le projet :**  
Influence directement la précision du binning dans `metrics.py`.

## L'assombrissement centre-bord (Limb Darkening)
**Définition :**  
Effet optique rendant le centre d'une étoile plus brillant que ses bords. Cela donne aux transits une forme en "U" plutôt qu'une boîte rectangulaire parfaite.  
**Contexte dans le projet :**  
Concept non modélisé mathématiquement ici (le BLS utilise un modèle de boîte), mais expliquant pourquoi les mesures de profondeur doivent se concentrer sur le centre du transit.