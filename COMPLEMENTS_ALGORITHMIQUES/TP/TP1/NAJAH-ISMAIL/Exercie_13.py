
#Q1
def Delta(a,b,c):
    ''' delta : (float,float,float) -> (float)
        calcule le discriminant du polynome '''
    return b**2 - (4*a*c)

#Q2
def nbRacine(a,b,c):
    ''' nbRacine : (float,float,float) -> int
        calcule le nombre de racine du polynome '''
    d = Delta(a,b,c)
    if d > 0:
        return 2
    if d < 0:
        return 0
    if d==0:
        return 1

#Q3
def racine1(a,b,c):
    ''' racine1 : (float,float,float) -> float
        calcule une racine du polynome '''
    return (-b+(Delta(a,b,c)**0.5))/2*a

def racine2(a,b,c):
    ''' racine1 : (float,float,float) -> float
        calcule la deuxieme racine du polynome'''
    return (-b-Delta(a,b,c)**0.5)/2*a

#Q4
def main():
    print "Programme de calcule d'un polynome de degree 2 :"
    p = input("valeur de a,b,c : ")
    d = Delta(p[0],p[1],p[2])
    print p[0],"x**2+",p[1],"x+",p[2],"a comme discriminant",d,"est a donc",nbRacine(p[0],p[1],p[2]),"racine(s) reelles :"
    if d == 0:
        print "x =",racine1(p[0],p[1],p[2])
    elif d > 0:
        print "x1 =",racine1(p[0],p[1],p[2])
        print "x2 =",racine2(p[0],p[1],p[2])

    

if __name__ == "__main__":
    main()