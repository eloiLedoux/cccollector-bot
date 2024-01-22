import carte
import recup_info

def construire_dico_infos(elagage):
    infos_def = {
        "nom" : elagage[1],
        "couleur" : elagage[2],
        "categorie" : elagage[3],
        "id" : elagage[0],
        "rarete" : elagage[4],
        "cout" : elagage[5],
        "puissance" : elagage[6],
        "attributs" : elagage[8],
        "types" : elagage[9],
        "contre" : elagage[7],
        "effet" : elagage[11]
    }
    return infos_def

def construire_dico_infos_fr(elagage):
    infos_def = {
        "nom" : elagage[1],
        "couleur" : elagage[2],
        "categorie" : elagage[3],
        "id" : elagage[0],
        "rarete" : elagage[4],
        "cout" : elagage[5],
        "puissance" : elagage[6],
        "attributs" : elagage[8],
        "types" : elagage[9],
        "contre" : elagage[7],
        "effet" : elagage[10]
    }
    return infos_def

def construire_carte(id_carte, fr=False):
    data = recup_info.requete_BDD(id_carte)
    if data == []:
        #ID associé à aucune carte
        return -1
    elagage = data[0]
    if fr:
        dico = construire_dico_infos_fr(elagage)
    else:
        dico = construire_dico_infos(elagage)
    print(dico)
    return carte.Carte(
        nom=dico["nom"],
        couleur=dico["couleur"],
        categorie=dico["categorie"],
        id=dico["id"],
        rarete=dico["rarete"],
        cout=dico["cout"],
        puissance=dico["puissance"],
        attributs=dico["attributs"],
        types=dico["types"],
        contre=dico["contre"],
        effet=dico["effet"]
    )

if __name__ == "__main__":
    carte = construire_carte('OP01-001')
    if carte == -1:
        print("Cette ID n'est associé à aucune carte.")
    else:
        print(carte.miseEnFormeFR())