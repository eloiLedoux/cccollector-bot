import psycopg2
import json

def requete_BDD(id_carte):
    with open('bdd-config.json', 'r') as cfg:
        configs = json.load(cfg) 
    #Etablir la connection:
    conn = psycopg2.connect(
    database=configs["database"], user=configs["user"], password=configs["password"], host=configs["host"], port=configs["port"]
    )
    #Creation du curseur pour requeter:
    cursor = conn.cursor()

    qry = "OP" + id_carte[2:]
    #Requete SQL:
    request = (f'SELECT * FROM public."Carte" WHERE code_carte = \'{qry}\'')
    cursor.execute(request)

    #Requetage (fetchall/fetchone/fetchmany(n))
    data = cursor.fetchall()
    #print("Données récupérées :",data)

    #Closing the connection
    conn.close()

    return data

if __name__ == "__main__":
    data = requete_BDD('OP01-001')
    print(data)