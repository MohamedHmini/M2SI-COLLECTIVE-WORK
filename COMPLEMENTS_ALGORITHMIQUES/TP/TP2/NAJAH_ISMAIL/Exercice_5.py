

def conversionDecVersStrBin(n):
    ''' conversionDecVersStrBin : (int) -> str
        prend en parametre un entier et retourne une chaine
        de caracteres qui represente sa conversion en base 2.'''
    return bin(n)[2:]

def conversionDecVersStrBase(n,b):
    ''' conversionDecVersStrBin : (int,int) -> str
        prend en parametre un entier et retourne une chaine
        de caracteres qui represente sa conversion en base b.'''
    result = []
    while n <> 0:
        result.append(str(n%b))
        n /= b
    else:
        reversed(result)
    return ''.join(result)


if __name__ == "__main__":
    print conversionDecVersStrBase(378,5)
    


pre = 0
current = 1
pres = current
current = pre+current
