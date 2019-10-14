from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import polynomeSolutionD2

def main():
    print("Programme de calcul d'un polynome de degré 2 (ax**2+bx+c) :")
    a,b,c=map(int,input("Donnez les valeurs de a,b et c :").split())
    print(polynomeSolutionD2(a,b,c))

if __name__=="__main__":
    main()