from ComplementsEnAlgorithmique.TP_1.Moad_Charhbili.My_Functions import percentage_red as app
def main():
    a = int(input("Indiquez le prix de l'article :"))
    b = int(input("Indiquez la valeur du reduction :"))
    a,b=app(a,b)
    print("L'article solde vous revient a ", a, " euros et ", b, " cent.")

if __name__ == "__main__":
    main()