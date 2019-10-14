from Python_Algo.TP_2.Moad_Charhbili.My_Functions import premier

def main():
    l=int(input("Saisir un entier : "))
    while l>=0:
        if premier(l):
            print(l , " est premiere")
        else:
            print(l, " n'est pas premiere")
        l = int(input("Saisir un entier : "))
if __name__ == '__main__':
    main()