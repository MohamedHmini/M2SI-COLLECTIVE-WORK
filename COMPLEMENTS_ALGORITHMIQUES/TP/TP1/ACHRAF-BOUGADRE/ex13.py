'''
delta : (float, float, float) --> (float)
calcule le discriminant du polynome
'''
def delta(a, b, c):
    return float(b)**2 - 4*float(a)*float(c)

'''
nbRacine : (float, float, float) --> (float)
calcule le nombre de racine du polynome
'''
def nbRacine(a, b, c):
    dlt = delta(a, b, c)
    if dlt > 0:
        return 2
    elif dlt == 0:
        return 1
    else :
        return 0

'''
racine1 : (float, float, float) --> (float)
calcule une racine du polynome
'''
def racine1(a, b, c):
    return (- float(b)-(delta(a, b, c)**0.5))/(a*2)

'''
racine2 : (float, float, float) --> (float)
calcule la deuxieme racine du polynome
'''
def racine2(a, b, c):
    return (- float(b)+(delta(a, b, c)**0.5))/(a*2)

if __name__=='__main__':
    print("Programme de calcule d'un polynome de degre 2 : ")
    a, b, c = map(int, raw_input('valeurs de a, b, c = ').strip('()').split(',') )

    discriminant = delta(a, b, c)
    nb_rac = nbRacine(a, b, c)
    
    print "%dx**2 + %dx + %d a comme discriminant %d et a donc %d racine(s) reelles" % (a, b, c , discriminant, nb_rac)
    if nb_rac >= 1:
        print "x1 = " + str(racine1(a, b, c))
        if nb_rac == 2:
            print "x2 = " + str(racine2(a, b, c))
