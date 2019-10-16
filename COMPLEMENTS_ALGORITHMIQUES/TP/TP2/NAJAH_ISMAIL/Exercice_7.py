
def test(m,n):
    if m==0:
        return 0
    if m%2==0:
        return test(m/2,n*2)
    return n+test(m-1,n)


def multEgyptienne(m,n):
    ''' multEgyptienne : (int,int) -> int
    la multiplication egyptienne utilise la multiplication
    par deux et la division par deux, ainsi que l addition.'''
    if m==0:
        return 0
    result = 0
    p=1
    while m>0:
        if m%2==0:
            m/=2
            p*=2
        else:
            result+=n*p
            m-=1
    return result

def main():
    n,m = input("n,m = ")
    if n<m:
        n,m = m,n
    print multEgyptienne(m,n)

if __name__ == "__main__":
    main()