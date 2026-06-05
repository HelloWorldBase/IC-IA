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