def CheckHeureSyntaxe(a,b,c):
    if  not a <= 23 and not a>=0:
        print("l'heure est obligée d'etre entre 0 et 23!!")
        return -1
    if not b <= 59 and not b >= 0:
        print("les minutes sont obligées d'etre entre 0 et 59!!")
        return -1
    if not c <= 59 and not c >= 0:
        print("les secondes sont obligées d'etre entre 0 et 59!!")
        return -1
    return 1
def CalculeDuree(a,b,c):
    if CheckHeureSyntaxe(a,b,c):
        return a*3600+b*60+c
    print("Error")
    return -1


def CalculeDifferenceHeure(a1,b1,c1,a2,b2,c2):
    s1,s2=0,0
    s1=CalculeDuree(a1,b1,c1)
    s2=CalculeDuree(a2,b2,c2)
    if CheckHeureSyntaxe(a1,b1,c1) and CheckHeureSyntaxe(a2,b2,c2):
        s1 = CalculeDuree(a1, b1, c1)
        s2 = CalculeDuree(a2, b2, c2)
        return abs(s1-s2)
    else:
        print("Error !!!!")
        return -1

def secondToHours(s):
    return int(s/3600),int((s%3600)/60),s%60

def PetitGrand(a,b):
    petit,grand=0,0
    petit, grand = 0, 0
    a = int(input("Donne le premiere nombre"))
    b = int(input("Donne le deuxieme nombre"))
    print(petit, "est plus petit ou egale a ", grand)
    return petit,grand

def pui2(a):
    return a**2
def pui4(a):
    return pui2(a)**2

def distance(a,b):
    """ Calculer la distance entre deux points x:(x1,x2) et y:(y1,y2)"""
    return ((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5

def dans_cercle(c,r,p):
    """ Verifier si une point appartient a une cercle ou pas, elle retourne True or False"""
    if distance(p,c)<=r:
        return True
    else:
        return False

def delta(a,b,c):
    return b**2-4*a*c
def nbRacines(a,b,c):
    d=delta(a,b,c)
    if d==0:
        return 1
    elif d>0:
        return 2
    else:
        return 0

def UnRacine(a,b,c):
    return (-b-delta(a,b,c)**2)/(2*a)
def DeuxRacine(a,b,c):
    return (-b-delta(a,b,c)**2)/(2*a),(-b+delta(a,b,c)**2)/(2*a)
def polynomeSolutionD2(a,b,c):
    print("Le discriminent : ", delta(a,b,c))
    if nbRacines(a,b,c)==2:
        print("Ce polynome a 2 racines.")
        return DeuxRacine(a,b,c)
    elif nbRacines(a,b,c)==1:
        print("Ce polynome a un seul racines.")
        return UnRacine(a,b,c)
    else:
        print("Ce polynome n'a aucun racine.")
        return -1

def Premier():
    a=int(input("Donner un nombre :"))
    d=2
    while d<a**0.5:
        if a%d==0:
            print(a," n'est pas premier ")
            break
        d=d+1
    else:
        print(a," est premier")

def perimiteRectangle(lon,lar):
    return 2*lar+2*lon

def airRectangle(x,y):
    return x*y

def percentage(prix,per):
    return prix*per/100
def percentage_red(prix,per):
    v=prix - percentage(prix, per)
    return int(v),int(40*(v%1))+1 if 40*(v%1)>0.5 else int(40*(v%1))