import requests
import json

def requete_API(id_carte):
    with open('api-config.json', 'r') as cfg:
        configs = json.load(cfg)
    protocol = "http://"
    database = "cartes"
    element = "code_carte"
    operator = "eq."
    URI = protocol + configs["address"] + ":" + configs["port"] + "/" + database + "?" + element + "=" + operator + id_carte
    
    reponse_API = requests.get(URI)
    data = reponse_API.text
    dico = json.loads(data)

    if dico == []:
        #ID associé à aucune carte
        return -1
    return dico[0]

if __name__ == "__main__":
    data = requete_API('OP01-001')
    if data == -1:
        print("Cette ID n'est associé à aucune carte.")
    else:
        print(data)