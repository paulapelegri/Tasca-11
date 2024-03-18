class Animal():
    def __init__(self, atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar():
        pass
    def mourem ():
        pass 
    def quisoc():
        print("Sóc un animal.")

class Cavall(Animal):
    def xerrar():
        print("Iíííííí")
    def mourem ():
        print("Em moc a trot")
    def quisoc():
        print("Sóc un Cavall")

class Dofi(Animal):
    def xerrar(self):
        print("IchIchIch")
    def mourem (self):
        print("Em moc nadant")
    def quisoc(self):
        print("Sóc un Dofí")

class Abella(Animal):
    def xerrar(self):
        print("Sssssssssss")
    def mourem (self):
        print("Em moc volant")
    def quisoc(self):
        print("Sóc un Abella")
    def picar(self):
        print("si m'emprenyes et picaré!")

class Huma(Animal):
    def __init__(self, nom, atribut, edat):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        print("Hola! Nosaltres utilitzem un idioma per parlar")
    def mourem (self):
        print("Em moc caminant")
    def quisoc(self):
        print("Sóc un Humà")

class Centaure(Huma, Cavall):
    def xerrar(self):
        print("Hola! Nosaltres utilitzem un idioma per parlar")
    def mourem (self):
        print("Em moc a trot")
    def quisoc(self):
        print("Sóc un Centaure")

class Fiet(Huma):
    def __init__(self, nom, atribut, edat, llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares
    def xerrar(self):
        print("Ueeeuee")
    def mourem (self):
        print("Em moc gatetjant")
    def quisoc(self):
        print("Sóc un Fiet")
    def nompares(self):
        for e in self.pares:
            print(e.nom)

class xou():
    def xerrar(self):
        print("Xou")
    def mourem (self):
        print("Em moc fent xou")
    def quisoc(self):
        print("Sóc un Xou")

#PP
a=[Cavall("Marró, 4"), Dofi("gris", "10"), Abella("negre i groga","0,5"), Huma("Sibila", "Cristià", "7"), Centaure("Fiona", "Marrón", "18"), Fiet("Jordi", "Moreno", "9",["Fiona", "Marc"]), xou()]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()