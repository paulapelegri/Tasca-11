def ajuntar(l,d,c):
    a=[]
    for i in range(len(l)):
        a.append(l[i]+c+d[i])
    print("La unió de les llistes {} i {} és {}".format(l,d,a))

#PP
l=["Super", "Hiper", "Mini", "Maxi"]
d=["women", "bole", "Mouse", "Boom"]
ajuntar(l,d,"-")
