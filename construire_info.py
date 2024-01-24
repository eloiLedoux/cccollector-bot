import carte
import recup_info

def construire_carte(id_carte, fr=False):
    data = recup_info.requete_API(id_carte)
    if data == -1:
        #ID associé à aucune carte
        return -1
    if fr:
        return carte.Carte(
            nom=data["nom"],
            couleur=data["couleur"],
            categorie=data["categorie"],
            id=data["code_carte"],
            rarete=data["rarete"],
            cout=data["cout"],
            puissance=data["puissance"],
            attributs=data["attribut"],
            types=data["type"],
            contre=data["contre"],
            effet=data["effet"]
        )

    return carte.Carte(
            nom=data["nom"],
            couleur=data["couleur"],
            categorie=data["categorie"],
            id=data["code_carte"],
            rarete=data["rarete"],
            cout=data["cout"],
            puissance=data["puissance"],
            attributs=data["attribut"],
            types=data["type"],
            contre=data["contre"],
            effet=data["texte_origine"]
    )

if __name__ == "__main__":
    carte = construire_carte('OP01-001', True)
    if carte == -1:
        print("Cette ID n'est associé à aucune carte.")
    else:
        print(carte.miseEnFormeFR())