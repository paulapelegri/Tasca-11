"ex12"
def ex10():
    a=[1, 2, 3, 4, 5]
    b=[6, 7, 8, 9, 10]
    c=list(zip(a,b))
    print(c)

"ex13"

def ex11():
    a=[1, 2, 3, 4, 5]
    b=list(filter(lambda x: x%2==1,a))
    print(b)

"ex14"

class Ordinador(a):
    def __init__(self, tipus, pantalla):
        self.tipus=tipus
        self.pantalla=pantalla

"ex15"

"ex16"

"ex17"

"ex18"

"ex19"

def ex12():
    a=[Portatil(), Tablet(), Servidor(), PC()]
    for e in a:
        e.getTipus()
        e.getPantalla()

"ex20"

def ex13():
    with open("/home/cicles/AO/ex20.txt", "w") as f:
        for i in range(10):
            f.write(i+"\n")
    with open("/home/cicles/AO/ex20.txt", "r") as f:
        for i in f:
            print(i)

