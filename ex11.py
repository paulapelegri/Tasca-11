def imprimir_fitxer(m):
    a=[]
    with open(m, "r") as f:
        for e in f:
            c= e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def afegir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.write(e+"\n")

#PP
fitxer="/home/cicles/AO/ex11.txt"
llista= ["Jordi", "Claudia", "David", "Ayoub", "Oscar", "Paula", "Clara"]
afegir_fitxer(fitxer,llista)
imprimir_fitxer(fitxer)
