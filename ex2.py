from functools import reduce
def Passar_a_numero(llista):
    a=list(map(lambda a: str(a),llista))
    b=reduce(lambda x,y:x+y,a)
    print("La llista {} és el número {}".format(llista,b))

 #PP
a=[3, 4, 1, 5,]
Passar_a_numero(a)