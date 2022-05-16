class humain:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.poids = 0
        self.taille = 0
        self.sexe = ""
        self.degats = 0
        self.vie = 100
        self.vie_max = 100
        self.vie_min = 0
        self.vie_actuelle = 100
        self.weapon = ""
        self.armure = ""
        self.arme_dmg = 0
        self.armure_dmg = 0
        self.armure_dmg_max = 0
        self.armure_dmg_min = 0
        self.armure_dmg_actuelle = 0
    # humain frappe avec armes
    def frappe(self, ennemi):
        print(self.nom + " frappe " + ennemi.nom)
        ennemi.degats(self.age)

    # humain recoit des degats
    def degats(self, age):
        if age < 18:
            self.degats = self.degats + 5
        elif age >= 18 and age <= 30:
            self.degats = self.degats + 10
        elif age > 30:
            self.degats = self.degats + 15
        else:
            self.degats = self.degats + 20
        self.vie_actuelle = self.vie_actuelle - self.degats
        if self.vie_actuelle <= 0:
            print(self.nom + " est mort")
        else:
            print(self.nom + " a " + str(self.vie_actuelle) + " points de vie")

    # humain recoit des soins
    def soins(self, soins):
        self.vie_actuelle = self.vie_actuelle + soins
        if self.vie_actuelle > self.vie_max:
            self.vie_actuelle = self.vie_max
        print(self.nom + " a " + str(self.vie_actuelle) + " points de vie")

    # humain recoit des degats
    def degats_recu(self, degats):
        self.vie_actuelle = self.vie_actuelle - degats
        if self.vie_actuelle <= 0:
            print(self.nom + " est mort")
        else:
            print(self.nom + " a " + str(self.vie_actuelle) + " points de vie")

    # humain recoit des soins
    def soins_recu(self, soins):
        self.vie_actuelle = self.vie_actuelle + soins
        if self.vie_actuelle > self.vie_max:
            self.vie_actuelle = self.vie_max
        print(self.nom + " a " + str(self.vie_actuelle) + " points de vie")

    # def str(self):
    #     return self.nom + " a " + str(self.vie_actuelle) + " points de vie"

    def __str__(self):
        #     return self.nom + " a " + str(self.vie_actuelle) + " points de vie"
        return "son nom est : " + self.nom +" et son age est de " + str(self.age) + " ans" + " a " + str(self.vie_actuelle) + " points de vie"
    def __repr__(self):
        return "humain(" + self.nom + "," + str(self.age) + ")"
    def __add__(self, other):
        return humain(self.nom + other.nom, self.age + other.age)
    def __sub__(self, other):
        return humain(self.nom + other.nom, self.age - other.age)
    def __mul__(self, other):
        return humain(self.nom + other.nom, self.age * other.age)
    def __truediv__(self, other):
        return humain(self.nom + other.nom, self.age / other.age)
    def __floordiv__(self, other):
        return humain(self.nom + other.nom, self.age // other.age)
    def __mod__(self, other):
        return humain(self.nom + other.nom, self.age % other.age)
    def __pow__(self, other):
        return humain(self.nom + other.nom, self.age ** other.age)
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    def __eq__(self, other):
        return self.age == other.age
    def __ne__(self, other):
        return self.age != other.age
    def __gt__(self, other):
        return self.age > other.age
    def __ge__(self, other):
        return self.age >= other.age
    def __and__(self, other):
        return humain(self.nom + other.nom, self.age & other.age)
    def __or__(self, other):
        return humain(self.nom + other.nom, self.age | other.age)
    def __xor__(self, other):
        return humain(self.nom + other.nom, self.age ^ other.age)
    def __lshift__(self, other):
        return humain(self.nom + other.nom, self.age << other.age)
    def __rshift__(self, other):
        return humain(self.nom + other.nom, self.age >> other.age)
    def __invert__(self, other):
        return humain(self.nom + other.nom, ~self.age)
    def __neg__(self, other):
        return humain(self.nom + other.nom, -self.age)
    def __pos__(self, other):
        return humain(self.nom + other.nom, +self.age)
    def __heat__(self, other):
        return humain(self.nom + other.nom, self.age ** other.age)
    #humain attaque
    def attaque(self, other):
        print(self.nom + " attaque " + other.nom)
        other.degats(self.age)
class robot:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.vie_max = 100
        self.vie_actuelle = 100

    # robot recoit des degats
    def degats(self, degats):
        self.vie_actuelle = self.vie_actuelle - degats
        if self.vie_actuelle <= 0:
            print(self.nom + " est mort")
        else:
            print(self.nom + " a " + str(self.vie_actuelle) + " points de vie")

    def attaque(self, other):
        print(self.nom + " attaque " + other.nom)
        other.degats(self.age)
    def __str__(self):
        return "son nom est : " + self.nom + " et son age est de " + str(self.age) + " ans"
    # robot recoit des degats
    def recoit_degats(self, degats):
        self.vie_actuelle = self.vie_actuelle - degats
        if self.vie_actuelle <= 0:
            print(self.nom + " est mort")
        else:
            print(self.nom + " a " + str(self.vie_actuelle) + " points de vie")

    # robot recoit des soins
    def recoit_soins(self, soins):
        self.vie_actuelle = self.vie_actuelle + soins
        if self.vie_actuelle > self.vie_max:
            self.vie_actuelle = self.vie_max
        print(self.nom + " a " + str(self.vie_actuelle) + " points de vie")

class humain_robot:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def __str__(self):
        return "son nom est : " + self.nom + " et son age est de " + str(self.age) + " ans"

# main
if __name__ == "__main__":
    print("Bonjour dans notre jeu developpé par hichem")
    name = input("Entrez votre nom : ")
    if name == "hichem":
        print("you are the boss  " + name)
    elif name == "darshan":
        print("tu es nul " + name + " et tu vas mourir")
    else:
        print("sort de la, " + name)
    age = int(input("Entrez votre age : "))
    h = humain(name, age)
    print(h)
    h.vie_actuelle = int(input("quelle sont ses points de vie ? "))
    # h.vie_actuelle = 85
    h.armure = int(input("quelle est le niveau de son armure ? "))
    if h.armure > 9:
        print("ohh lalalala mais c'est une armre legendaire")
    # h.armure = 10
    # h.degats_recu(10)
    robot_name = input("Entrez le nom du robot : ")
    robot_age = int(input("Entrez son age : "))
    r = robot(robot_name, robot_age)
    r.armure = int(input("quelle est le niveau de son armure ? "))
    if r.armure < 9:
        print("armure ta3ek tafha ya : ",robot_name)
    r.vie_actuelle = int(input("quelle sont ses points de vie ? "))
    h.frappe(r)
    h.attaque(r)

    h.degats=int(input("quelle sont les degats qu'il inflige ? "))
    # h.degats(10)
    r.recoit_degats(h.degats)
    print(h)
    # print(robot_name + " a " + str(robot_age) + " points de vie")
    # robot_name = input("Entrez le nom du robot : ")
    # robot_age = int(input("Entrez son age : "))
    print(r)
    h.attaque(r)
    print(r)
    r.attaque(h)
    print(h)
    h.attaque(r)
    print(r)
    r.attaque(h)
    print(h)
    h.attaque(r)
    print(r)
    hr = humain_robot("cyborg", 1)
    # print(hr)