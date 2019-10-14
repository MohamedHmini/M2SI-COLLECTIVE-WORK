from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import perimiteRectangle as per
from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import airRectangle as air

def main():
    a,b=map(int,input("Entrz les dimensions (longueur,largeur) de votre rectangle :").split())
    print("Choisissez :")
    print("1-Je veux connaitre le perimetre du rectangle:")
    print("2-Je veux connaitre l'air du rectangle:")
    c=int(input('Votre choix:'))
    if c==1:
        print("Le perimetre de votre rectangle est : ",per(b,a))
    elif c==2:
        print("L'air de votre rectangle est : ",air(b,a))
    else:
        print("Choix erroné!!")

if __name__=="__main__":
    main()