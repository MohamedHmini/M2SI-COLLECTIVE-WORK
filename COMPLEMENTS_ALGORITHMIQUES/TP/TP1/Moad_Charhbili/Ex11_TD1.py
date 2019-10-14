from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import pui2,pui4

def main():
    a=int(input("Saisir un entier :"))
    print("Le carre de ",a," est : ",pui2(a))
    a = int(input("Saisir un entier :"))
    print("La puissance quatrième de ",a," est : ", pui4(a))

if __name__=="__main__":
    main()