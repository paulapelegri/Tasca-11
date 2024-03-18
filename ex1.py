def lenp(frase):
    b=frase.split(" ")
    c=list(map(len, b))
    print("La frase {} té les següents longituds {}".format(frase,c))

#PP
frase=input("Escriu una frase: ")
lenp(frase)