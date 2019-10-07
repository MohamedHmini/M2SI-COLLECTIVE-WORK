def pui2(nombre):
    return nombre**2

if __name__=='__main__':
    nb = int(raw_input('Saisire un entier : '))
    print "Le carre de %d est %d" % (nb, pui2(nb))
