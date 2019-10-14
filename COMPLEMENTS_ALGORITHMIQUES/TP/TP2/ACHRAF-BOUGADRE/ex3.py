def premier(n):
    racine = int(n**0.5 + 1)
    for i in range(2, racine ):
        if n % i == 0 :
            return False
    else :
        return True

if __name__=='__main__':
    while True:
        n = int(input('Entrez un nombre : '))
        if n <= 0 : 
            break

        if premier(n):
            print("%d est un nombre premier!"% n)
        else:
            print("%d n'est pas un nombre premier!"% n)