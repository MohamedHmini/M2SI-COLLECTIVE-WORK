from Python_Algo.TP_2.Moad_Charhbili.My_Functions import multEgyptienne,multEgyptienne_rec
def main():
    a,b = map(int,input('Saisir un entier : ').split())
    print(multEgyptienne(a,b))
    print(multEgyptienne_rec(a,b))
if __name__ == '__main__':
    main()