#Utilizamos una excepcion
def div(a,b):
    try:
        c=a/b
        print("La divisió de {} entre {} és {}".format(a,b,c))
    except ZeroDivisionError:
        print("El segon paràmetre no potser zero")

#PP
a=int(input("Escriu el numerador: "))
b=int(input("Escriu el denominador"))
div(a,b)