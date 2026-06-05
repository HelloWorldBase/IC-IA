import os

# Matrice complète des fichiers du Système B (Version v5 - Finale et Validée)
files = {
    # 1. Contrôleur d'accueil du dépôt
    "README.md": """
# 🌐 Système B - Infrastructure Citoyenne de Subsistance (Québec)

> **Statut du Contrôleur :** Phase d'amorçage. Transition systémique (A ➔ B) activée.
> **Modèle d'évaluation :** Homéostasie collective (Remplacement du PIB).
> **Cadre :** Design 4.0 & Prospective Fonctionnelle apolitique.

## 🎛️ Mode d'emploi de la Tâche Libre
Ce projet fonctionne de manière horizontale sans hiérarchie centralisée. Si vous voyez une tâche à faire ou un document à améliorer :
1. **Explorez** les enjeux locaux et les données physiques dans le dossier `/docs`.
2. **Déclarez** votre action ou un signal de terrain en ouvrant une *Issue* GitHub.
3. **Injectez** votre force de travail (0% bureaucratie, 100% valeur d'usage réelle).
""".strip(),

    # 2. Gabarits d'activation automatisés pour GitHub
    ".github/ISSUE_TEMPLATE/task_vigile.md": """
---
name: "🔍 Signalement Vigile (Niveau 1)"
about: Signaler un signal faible, un enjeu de subsistance ou une rupture locale dans le Système A.
title: "[VIGILE] : "
labels: ["Niveau 1", "Tâche Libre", "Prospective"]
---

## 🔍 IDENTIFICATION DU VIGILE (NIVEAU 1)
* **Rayon d'action géographique :** (Ex: Quartier Youville, 5 km)
* **Région administrative :** (Ex: Capitale-Nationale - Région 03)

## 🚨 NATURE DU SIGNAL OU DE LA RUPTURE (SYSTÈME A)
* [ ] **Alimentation** (Inflation, pénurie de grossistes, bris de chaîne d'approvisionnement)
* [ ] **Énergie / Logement** (Hausse des coûts, panne réseau, vulnérabilité thermique)
* [ ] **Logistique / Transport** (Rupture de distribution, transport de subsistance défaillant)

### Récit de terrain brut :
> *Décrivez ici de manière factuelle ce que vous observez à votre échelle locale.*
""".strip(),

    ".github/ISSUE_TEMPLATE/task_groupe.md": """
---
name: "👥 Activation Groupe Local (Niveau 2)"
about: Déployer l'Assurance Pré-Sinistre et coordonner les tâches libres.
title: "[GROUPE] : "
labels: ["Niveau 2", "Assurance Pré-Sinistre", "Action Terrain"]
---

## 👥 IDENTIFICATION DU GROUPE LOCAL
* **Nom de la cellule / Groupe :** (Ex: Collectif Youville, Le Pignon Bleu)
* **Région administrative d'ancrage :** 

## 💰 ALLOCATION DU CARBURANT ÉCONOMIQUE (1 $/MOIS)
* **Flux financier disponible ($) :** (Nombre de membres engagés × 1 $)
* **Infrastructure de subsistance visée par l'achat brut :**
    * [ ] **Alimentaire** (Terres nourricières, serres locales, semences rustiques, chambres froides)
    * [ ] **Énergétique** (Panneaux solaires distribués, isolation passive collective)
* **Montant total engagé :** ___________ $
""".strip(),

    # 3. Documents fondamentaux de la matrice
    "docs/01_systeme_b.md": """
# 🧬 Spécifications du Système B : Modèle d'Homéostasie Collective

* **Système A (Actuel) :** Capitaliste, basé sur le PIB, dépendant des hydrocarbures, générateur d'inflation et réactif.
* **Système B (Cible) :** Horizontal, basé sur l'homéostasie des fonctions vitales, activé par les tâches libres et armé de l'assurance pré-sinistre.
* **Règle du 1 $ :** Promesse d'investissement mensuel futur de 1 $ par citoyen. 100 % injecté sur le terrain au Niveau 2 pour acheter de la résilience physique. 0 % à la couche technologique ou à l'IA.
""".strip(),

    "docs/02_niveaux_ic.md": """
# 🌐 Architecture Fractale des 4 Niveaux d'Intelligence Collective

* **Niveau 1 : L'Individu** – Formulaire de diagnostic de subsistance, rayon d'action (5 km) et déclaration volontaire des tâches libres.
* **Niveau 2 : Le Groupe Local** – Cellules de 2 à 15 000 membres (Ex: Collectif Youville, Cuisines Collectives). Convertit la caisse commune en infrastructures physiques d'utilité publique.
* **Niveau 3 : La Nation** – Interconnexion horizontale des 17 régions administratives du Québec pour équilibrer les flux logistiques sans intermédiaire marchand.
* **Niveau 4 : Le Global** – L'ONU par la base reliant les collectifs open-source mondiaux.
""".strip(),

    "docs/03_ecoherence.md": """
# 🧬 Méthodologie Design 4.0 (Institut d'Écohérence)

* **Les Vigiles (Niveau 1) :** Assurent la veille terrain et détectent les failles du Système A.
* **Les Cartographes (Niveau 2) :** Relient les signaux et modélisent visuellement l'état des besoins et des ressources de subsistance.
* **Les Explorateurs (Niveau 2) :** Déploient matériellement les infrastructures d'autonomie grâce au budget pré-sinistre.
""".strip(),

    "docs/04_matrice_energetique.md": """
# ⚡ Paramétrage Énergétique du Système B (Données HEC Montréal)

* **Constat Système A :** L'État de l'énergie au Québec par HEC démontre que 60 % de l'énergie consommée par le secteur industriel est gaspillée ou perdue.
* **Règle d'étanchéité du Système B :** Interdiction d'investir la caisse citoyenne dans des solutions dépendantes de réseaux centralisés défaillants. Priorité absolue aux microréseaux thermiques, à la captation des rejets et à la sobriété locale.
""".strip(),

    # 4. Code source de la Vue Nationale (Les 17 régions et 51 groupes réels)
    "src/vue_regions.py": """
import os

# Base de données synaptique du Niveau 3 (Nation) - 3 groupes réels par région
regions_qc = {
    "01": {"nom": "Bas-Saint-Laurent", "vigiles": 12, "groupes": ["Carrefour d'Initiatives Populaires (CIP)", "Cuisines collectives de Cabano", "Croc Ensemble des Basques"], "infra_energie": "Biomasse locale", "statut": "COHÉRENT"},
    "02": {"nom": "Saguenay–Lac-Saint-Jean", "vigiles": 45, "groupes": ["Cuisines collectives de Jonquière", "Coopérative de solidarité Nord-Bio", "Le Maillon"], "infra_energie": "Micro-hydro", "statut": "SURPLUS EN ÉNERGIE"},
    "03": {"nom": "Capitale-Nationale", "vigiles": 150, "groupes": ["Collectif Youville [System B]", "Le Pignon Bleu [System B]", "La Baratte"], "infra_energie": "Serres thermiques", "statut": "CRITIQUE (ALIMENTATION)"},
    "04": {"nom": "Mauricie", "vigiles": 28, "groupes": ["Cuisines collectives de la Mauricie", "Le Festigoût / AGRO-Form", "Espace Famille Shawinigan"], "infra_energie": "Solaire passif", "statut": "COHÉRENT"},
    "05": {"nom": "Estrie", "vigiles": 64, "groupes": ["Aux p'tits oignons", "Moisson Estrie", "La Grande Table"], "infra_energie": "Réseau thermique décentralisé", "statut": "SURPLUS MARAÎCHER"},
    "06": {"nom": "Montréal", "vigiles": 310, "groupes": ["Carrefour Solidaire Centre-Sud [System B]", "Club populaire de Pointe-St-Charles", "Santropol Roulant"], "infra_energie": "Récupération pertes ind. (60% HEC)", "statut": "VULNÉRABILITÉ ÉNERGÉTIQUE"},
    "07": {"nom": "Outaouais", "vigiles": 19, "groupes": ["Racines des cuisines collectives de Gatineau", "La Manne de l'Île", "Coopérative de solidarité de l'Outaouais"], "infra_energie": "Bois d'œuvre/chauffage", "statut": "EN ATTENTE D'ACTIONS"},
    "08": {"nom": "Abitibi-Témiscamingue", "vigiles": 15, "groupes": ["Cuisines collectives d'Amos", "La Source d'Entraide de Rouyn-Noranda", "Coopérative de solidarité de la Vallée de l'Or"], "infra_energie": "Géothermie de surface", "statut": "COHÉRENT"},
    "09": {"nom": "Côte-Nord", "vigiles": 8, "groupes": ["Cuisines collectives de Sept-Îles", "Hommes Sept-Îliens", "Le Grain de Sel de Baie-Comeau"], "infra_energie": "Éolien citoyen", "statut": "DÉFICIT LOGISTIQUE"},
    "10": {"nom": "Nord-du-Québec", "vigiles": 3, "groupes": ["Chibougamau Cuisines Collectives", "Comité d'aide alimentaire de Lebel-sur-Quévillon", "Réseau d'entraide de Radisson"], "infra_energie": "Potentiel hydro isolé", "statut": "ISOLEMENT SYSTÉMIQUE"},
    "11": {"nom": "Gaspésie–Îles-de-la-Madeleine", "vigiles": 22, "groupes": ["Touski-Madeline [System B]", "Cuisines collectives de la Baie-des-Chaleurs", "Réseau Alimentaire de la Haute-Gaspésie"], "infra_energie": "Marémoteur/Éolien", "statut": "SURPLUS HALIEUTIQUE"},
    "12": {"nom": "Chaudière-Appalaches", "vigiles": 55, "groupes": ["Cuisines collectives de Lévis", "Le COMPTOIR de Beauce", "La Gigoteuse"], "infra_energie": "Agro-thermique décentralisé", "statut": "SURPLUS AGRICOLE"},
    "13": {"nom": "Laval", "vigiles": 40, "groupes": ["APARL", "Centre de bénévolat et moisson Laval", "Le Relais Communautaire de Laval"], "infra_energie": "Serres urbaines", "statut": "CRITIQUE (ESPACE NOURRICIER)"},
    "14": {"nom": "Lanaudière", "vigiles": 37, "groupes": ["Action Famille Lanoraie", "Cuisines collectives de la MRC de Joliette", "La Hutte"], "infra_energie": "Biogaz de ferme", "statut": "COHÉRENT"},
    "15": {"nom": "Laurentides", "vigiles": 48, "groupes": ["Cuisines collectives de Saint-Jérôme", "Le Coffret", "Moisson Laurentides"], "infra_energie": "Solaire de masse", "statut": "HAUSSE DE PRESSION"},
    "16": {"nom": "Montérégie", "vigiles": 120, "groupes": ["Actions Familles Ste-Martine", "Carrefour d'Entraide de Longueuil", "Cuisines collectives de Granby"], "infra_energie": "Biogaz / Récupération rejets", "statut": "SURPLUS MARAÎCHER EXTRÊME"},
    "17": {"nom": "Centre-du-Québec", "vigiles": 31, "groupes": ["Cuisines collectives de Drummondville", "L'Ensoleillée de Victoriaville", "La Tablée d'Arthabaska"], "infra_energie": "Éolien communautaire", "statut": "COHÉRENT"}
}

def afficher_vue_nationale():
    print("="*95)
    print("🌐 VUE CONTRÔLEUR (N3) : RÉPERTOIRE DES 51 GROUPES LOCAUX DE SUBSISTANCE DU QUÉBEC")
    print("="*95)
    print(f"{'Code':<5} | {'Région administrative':<30} | {'Vigiles':<8} | {'Groupes Locaux Principaux (Niveau 2)'}")
    print("-"*95)
    for code, data in regions_qc.items():
        groupes_str = ", ".join(data["groupes"])
        print(f"{code:<5} | {data['nom']:<30} | {data['vigiles']:<8} | {groupes_str}")
    print("="*95)

if __name__ == "__main__":
    afficher_vue_nationale()
""".strip()
}

# Génération automatisée des dossiers et fichiers de l'infrastructure
#print("🏗️ Initialisation de la structure du dépôt Git...")
for path, content in files.items():
    folder = os.path.dirname(path)
    if folder:os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:f.write(content)
    print("✅ Configuration terminée. Tous les fichiers et dossiers sont prêts à être poussés sur GitHub !")