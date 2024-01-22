class Carte:
    def __init__(self, nom, couleur, categorie, id, rarete, cout, puissance, attributs, types, contre, effet):
        self.nom = nom
        self.couleur = couleur
        self.categorie = categorie
        self.id = id
        self.rarete = rarete
        self.cout = cout
        self.puissance = puissance
        self.attributs = attributs
        self.types = types
        self.contre = contre
        self.effet = effet

    def miseEnForme(self):
        return (f"{self.nom} \n"
        f"{self.couleur} {self.categorie} / ({self.id}) {self.rarete} \n"
        f"Cost : {self.cout} / Power : {self.puissance} ({self.attributs}) \n"
        f"{self.types} \n"
        f"Counter : [{self.contre}] \n"
        f"{self.effet}")
    
    def miseEnFormeFR(self):
        return (f"{self.nom} \n"
        f"{self.categorie} {self.couleur} / ({self.id}) {self.rarete} \n"
        f"Coût : {self.cout} / Puissance : {self.puissance} ({self.attributs}) \n"
        f"{self.types} \n"
        f"Contre : [{self.contre}] \n"
        f"{self.effet}")
    
c1 = Carte("Oden", "Red", "Character", "OP18-001", "SEC", "10", "9000", "Slash", "Land of Wano", "0", "[Activate : Main] : win the game")
print(c1.miseEnForme())