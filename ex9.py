def pot(p):
    r=[x**p for x in range(1,10)]
    print("Les poténcies elevades a {} dels 10 primers numeros són {}".format(p,r))

#PP
p=int(input("Introdueixi un número al qual voleu elevar la resta: "))
pot(p)