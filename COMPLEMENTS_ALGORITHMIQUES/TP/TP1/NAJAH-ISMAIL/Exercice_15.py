

def pourcentage(x,prix):
    ''' pourcentage : (int,float) -> float
    calcule le x pourcent du prix'''
    return (float(prix*x))/100.0

def main():
    prix = input(" Indiquer le prix de l'article : ")
    x = input(" Indiquer la valeur de la reduction (en %) : ")
    solde = str(prix-pourcentage(x,prix)).split('.')
    print "L'article solde vous revient a",solde[0],"euro et",solde[1],"cent"

if __name__ == "__main__":
    main()