import ex11_1 

def pui4(nombre):
    return ex11_1.pui2(nombre) ** 2
    
if __name__=='__main__':
    nb = int(raw_input('Saisire un entier : '))
    print "Le puissance quatrieme de %d est %d" % (nb, pui4(nb))