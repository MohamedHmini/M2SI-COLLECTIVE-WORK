

def main():
    n = input("Saisir n : ")
    while n<0 or n>20:
        n = input("Erorr!! Saisir n : ")
    sp = n-1
    for i,j in zip(range(1,n+1),range(0,n)):
        print (" "*sp+'*'*(i+j))
        sp-=1

if __name__ == "__main__":
    main()