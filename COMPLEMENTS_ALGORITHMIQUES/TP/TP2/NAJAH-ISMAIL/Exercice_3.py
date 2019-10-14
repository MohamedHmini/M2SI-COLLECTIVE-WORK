

def premier(n):
    if n < 2 :
        print n,"est non premier"
        return
    i=2
    while i < n**0.5:
        if n%i==0:
            print n,"est non premier"
            break
        i+=1
    else:
        print n,"est premier"

def main():
    n = input("Entrer un nombre : ")
    while n >= 0:
        premier(n)
        print " ------------ "
        n = input("Entrer un nombre : ")

if __name__ == "__main__":
    main()
