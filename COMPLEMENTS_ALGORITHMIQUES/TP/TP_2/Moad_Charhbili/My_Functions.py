def premier(a):
    if a==0 or a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def sommeDiviseurs(a):
    l=[i for i in range(1,int(a/2)+1) if a%i==0]
    return sum(l)

def conversionDecVersStrBin(a):
    s=''
    while a>=1:
        s=str(int(a)%2)+s
        a=int(a/2)
    return s
def conversionDecVersStrBase(a,b):
    s=''
    while a>=1:
        s=str(int(a)%b)+s
        a=int(a/b)
    return s
def fibonacciNp1(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciNp1(n-1)+fibonacciNp1(n-2)

def multEgyptienne_rec(m,n):
    if m==0:
        return 0
    elif m%2==0:
        return multEgyptienne_rec(m/2,2*n)
    elif m%2!=0:
        return n+multEgyptienne_rec(m-1,n)

def multEgyptienne(m,n):
    t,d={},{}
    k=m
    while k>0:
        if k%2==0:
            n*=2
            k = int(k / 2)
            t[k]=n

        if k%2==1:
            k=k-1
            d[k]=n

    return sum(d.values())