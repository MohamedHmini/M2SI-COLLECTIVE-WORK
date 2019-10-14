def conversionDecVersStrBin(n:int) -> str:
    s = []
    while n != 0:
        s.append( '1' if n & 1 == 1 else '0' )
        n >>= 1
    else:
        return ''.join(s[::-1])

def conversionDecVersStrBase(n , base):
    s = []
    while n != 0:
        s.append( str( n%base ) )
        n //= base
    else:
        return ''.join(s[::-1])

if __name__ == "__main__":
    print( conversionDecVersStrBin(338) )
    print( conversionDecVersStrBin(12) )

    print(conversionDecVersStrBase(338,5))