from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import CalculeDifferenceHeure,secondToHours

def main():
    a,b,c = map(int,input("Saisir l'heure 1 (hh:mm:ss) :").split(":"))
    a1,b1,c1 = map(int,input("Saisir l'heure 2 (hh:mm:ss) :").split(":"))
    temp= CalculeDifferenceHeure(a,b,c,a1,b1,c1)
    print("Difference : ",temp)
    temp=secondToHours(temp)
    print(" ### ",temp[0],':',temp[1],':',temp[2])

if __name__ == '__main__':
    main()