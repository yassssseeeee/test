from numpy import*

def saisie ():

    valide=False

    while valide==False :

        n=int(input("Donner n "))

        valide=4<=n<=20

    return n


def remplir (n,t):

    for i in range(n):

        valide=False

        while valide==False:

            t[i]=input("t["+str(i)+"]")

            valide=verif(t[i])
            

def verif(ch):

    test=True

    for i in range (len(ch)):

        if not("A"<=ch[i]<="Z" or "a"<=ch[i]<="z"):

            test=False

    return test


def remplirV (n,t,V):

    for i in range(n):

        f=0

        for j in range (len(t[i])):

            if t[i][j] in {"A","a","I","i","E","e","U","u","O","o","Y","y"}:

                f=f+1

            V[i]=f
            
def jls_extract_def():
    
    return 


def maximum (n,V):

    max=V[0] = jls_extract_def()
    for i in range(1,n):

        if V[i]>max:

            max=V[i]

    return max


def affiche (n,t,V,max):

    for i in range (n):

        if max==V[i]:

            print (t[i])


#p.p

t=array([str]*20)

V=array([int()]*20)
n=saisie()

remplir(n,t)

max=maximum (n,V)

affiche (n,t,V,max)