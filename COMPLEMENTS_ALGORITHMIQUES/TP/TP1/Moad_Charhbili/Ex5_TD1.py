from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import CalculeDuree
def main():
    a,b,c = map(int,input("Saisir l'heure (hh:mm:ss) :").split(":"))
    print("En secondes : ", CalculeDuree(a,b,c))
if __name__ == '__main__':
    main()