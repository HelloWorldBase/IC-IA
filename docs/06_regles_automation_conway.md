# 🎛️ Spécifications d'Automatisation : Modèle Conway (Jeu de la Vie)

Ce document définit les règles de transition mathématiques du Système B. Le contrôleur distribué utilise les principes des automates cellulaires de John Conway pour réguler l'apparition, la scission ou la fusion des cellules citoyennes sans aucune autorité centrale.

---

## 📐 Les Règles d'Or de l'Automate Territorial (Grille de 5 km)

Le territoire du Québec est modélisé comme une grille où chaque case représente le rayon d'action de subsistance d'un individu (Niveau 1 : 5 km). L'état d'une cellule locale (Niveau 2) évolue à chaque cycle d'évaluation selon l'état de ses voisins immédiats.

### 1. La Règle d'Isolement (Sous-population)
*   **Condition :** Toute cellule locale (Niveau 2) qui compte moins de 2 cellules voisines actives ou dont l'effectif tombe sous le seuil critique d'engagement.
*   **Résultat :** La cellule entre en état de vulnérabilité. Le système déclenche automatiquement une alerte de maillage horizontal au Niveau 3 pour commander sa fusion avec le groupe local actif le plus proche dans la région administrative.

### 2. La Règle d'Homéostasie (Stabilité)
*   **Condition :** Toute cellule locale entourée de 2 ou 3 cellules voisines actives et dont la taille reste comprise entre **2 et 15 000 membres**.
*   **Résultat :** La cellule survit et se stabilise. Elle atteint l'état de *Still Life* (structure stable). Ses flux logistiques d'eau, d'alimentation et d'énergie s'auto-équilibrent avec son environnement immédiat.

### 3. La Règle de Mitose Fractale (Surpopulation)
*   **Condition :** Toute cellule locale qui dépasse le seuil critique de **15 000 membres** ou qui subit une surcharge bureaucratique étouffant la valeur d'usage.
*   **Résultat :** La cellule « meurt » sous sa forme centralisée pour renaître instantanément par mitose fractale. Elle se divise en deux nouvelles cellules locales autonomes et adjacentes pour préserver l'agilité et l'horizontalité du modèle.

### 4. La Règle d'Émergence (Naissance)
*   **Condition :** Toute zone territoriale inactive qui se retrouve entourée d'exactement 3 signaux faibles convergents ou 3 Vigiles actifs (Niveau 1) signalant une même faille du Système A.
*   **Résultat :** Une nouvelle cellule de Niveau 2 « naît » organiquement dans le Réservoir Systémique. Une Caisse Commune locale est initialisée et la transition vers le Système B est activée à cet emplacement précis.

---

## 🚢 Les Structures Émergentes du Niveau 3 (Logistique)

À l'échelle de la Nation (Niveau 3), l'interaction de ces règles locales fait apparaître des configurations macroscopiques bien connues du Jeu de la Vie, détournées pour la résilience physique :

*   **Les Oscillateurs (Stocks Tampons) :** Structures locales qui alternent périodiquement entre deux états (ex : surproduction agricole en été ↔ consommation des réserves en hiver). Ils régulent le rythme circadien et saisonnier de la subsistance sans nécessiter de planification étatique.
*   **Les Gliders / Vaisseaux (Flux Logistiques) :** Structures physiques de ressources qui se déplacent de case en case à travers les 17 régions administratives. Un surplus de bois d'œuvre ou de semences se propage horizontalement le long du réseau jusqu'à rencontrer une cellule locale en état de besoin (sous-population de ressources), où il se stabilise.

---

## 🎛️ Activation par la Tâche Libre

Ce moteur de règles exclut tout arbitrage humain ou technologique lourd (0% IA). Les citoyens alimentent directement la grille :
1. **Consultez l'état de la grille** locale dans votre dossier régional `/docs`.
2. **Si votre cellule est isolée :** Déclarez une Tâche Libre de maillage avec la cellule voisine.
3. **Si votre cellule s'approche des 15 000 membres :** Ouvrez une *Issue* GitHub pour planifier la mitose architecturale de votre collectif.
