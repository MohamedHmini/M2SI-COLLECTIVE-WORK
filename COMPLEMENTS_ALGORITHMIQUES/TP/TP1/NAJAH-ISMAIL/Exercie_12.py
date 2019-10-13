

def dist(a,b):
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5

def dans_cercle(C,p):
    return dist(C[0],p) < C[1]

def dans_intersection(C1,C2,p):
    return dans_cercle(C1,p) and dans_cercle(C2,p)

o1 = input(" Entrer les coordonees du centre du cercle 1 (x,y) : ")
r1 = input("Entre le rayon du cercle 1 : ")
C1 = (o1,r1)
o2 = input(" Entrer les coordonees du centre du cercle 2 (x,y) : ")
r2 = input("Entre le rayon du cercle 2 : ")
C2 = (o2,r2)
p = input(" Entrer les coordonees du point (x,y) : ")
print dans_intersection(C1,C2,p)
