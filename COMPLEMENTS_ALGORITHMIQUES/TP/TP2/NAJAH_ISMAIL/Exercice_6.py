

cach = {0:0,1:1}
def fibo(n):
    ''' fibo : (int) -> int
    retourne la valeur du (n+1) eme terme de 
    la suite de Fibonacci.'''
    if n<2:
        return cach[n]
    for i in range(2,n+2):
        cach[i] = cach[i-1]+cach[i-2]
    return cach[n+1]

def main():    
    n=input("n = ")
    fibo(n)
    print ' '.join([str(x) for x in cach.values()])

if __name__ == "__main__":
    main()