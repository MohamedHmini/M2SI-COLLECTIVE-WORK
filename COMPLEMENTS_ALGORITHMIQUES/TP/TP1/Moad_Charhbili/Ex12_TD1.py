from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import distance
from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import dans_cercle

def main():
    print("Choisissez ce que tu veut faire :")
    print("1) Calcule la distance entre deux points.")
    print("2) Verifier si une point appartient a une cercle.")
    print("3) Verifier si une point appartient a l'intersection de deux cercles.")
    a=int(input(" ########## Votre Choix : ##########\n"))
    if a==1:
        a=tuple(map(int,input("Entrez les coordonnées de votre premiere point a :").split(',')))
        b=tuple(map(int,input("Entrez les coordonnées de votre deuxieme point b :").split(',')))
        print(" La distance entre les deux point est de : ",distance(a,b))
    if a==2:
        a = tuple(map(int, input("Entrez les coordonnées de votre cercle :").split(',')))
        b = int(input("Entrez le rayon de votre cercle :"))
        c = tuple(map(int, input("Entrez les coordonnées du point :").split(',')))
        if dans_cercle(a,b,c):
            print("Votre point appartient a cette cercle")
        else:
            print("Votre point n'appartient pas a cette cercle")
    if a==3:
        a = tuple(map(int, input("Entrez les coordonnées de votre premiere cercle :").split(',')))
        b = int(input("Entrez le rayon de votre premiere cercle :"))
        d = tuple(map(int, input("Entrez les coordonnées de votre deuxime cercle :").split(',')))
        e = int(input("Entrez le rayon de votre deuxieme cercle :"))
        c = tuple(map(int, input("Entrez les coordonnées du point :").split(',')))
        if dans_cercle(a, b, c) and dans_cercle(d,e,c):
            print("Votre point appartient a cette cercle")
        else:
            print("Votre point n'appartient pas a cette cercle")

if __name__=="__main__":
    main()