

def perimetreRec(width,hight):
    ''' perimetreRec : (float,float) -> float
        calcule le perimetre d'un rectangle'''
    return (width+hight)*2

def aireRec(width,hight):
    ''' airRec : (float,float) -> float
        calcule l'aire d'un rectangle'''
    return width*hight

def main():

    dim = input(" Entrer les dimention (longeur,largeur) de votre rectongle : ")
    print "Choisissez : "
    print "1- je veux connaitre le perimetre du rectangle"
    print "2- je veux connaitre l'aire' du rectangle"
    op = input("Votre choix : ")
    while op <= 0 or op > 2:
        op = input("Error !! Votre choix : ")
    if op == 1:
        print "le perimetre est :",perimetreRec(dim[1],dim[0])
    else:
        print "l'aire' est :",aireRec(dim[1],dim[0])

if __name__ == "__main__":
    main()