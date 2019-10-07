def pourcentage(x, prix):
    return (float(prix) * (float(x) / 100))

def solde(prix, reduction):
    return prix - pourcentage(reduction, prix)

if __name__ == "__main__":
    prix = int(raw_input("Idiquez le prix de l'article : "))
    reduction = int(raw_input("Idiquez la valeur de la reduction (en %) : "))
    sld = solde(prix, reduction)
    print "L'article solde vous revient a %d euros."%(sld)
