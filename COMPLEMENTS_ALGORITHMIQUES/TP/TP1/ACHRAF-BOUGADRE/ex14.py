def calcPerimetre(hight, width):
    return (hight + width)*2

def calcAire(hight, width):
    return (hight * width)

if __name__ == "__main__":
    print "Entrez les dimensions (longueur, largeur) de votre rectangle :"
    print "\n Choisissez : "
    print "1- je veux connaitre le perimetre du rectangle"
    print "2- je veux connaitre l'aire du rectangle"

    functions = (calcPerimetre, calcAire)
    while True:
        choix = int(raw_input("\nVotre choix : "))
        if choix == 1 or choix == 2:
            hight, width = map(int, raw_input('Gime me the : height width : ').split())
            print functions[choix - 1](hight, width)
            break
            