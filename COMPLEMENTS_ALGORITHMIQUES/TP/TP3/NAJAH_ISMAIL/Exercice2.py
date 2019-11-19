
cach = []
def isHammingNumber(n):
    global cach
    if n in cach:
        return True
    if n==1:
        return True
    if n%2==0:
        return isHammingNumber(n//2)
    if n%3==0:
        return isHammingNumber(n//3)
    if n%5==0:
        return isHammingNumber(n//5)
    return False

def HammingSeq(n):
    global cach
    if n==1:
        return 1
    for i in range(1,n+1):
        if isHammingNumber(i):
            cach.append(i)
            print(i,end=" ")


def main():
    n = int(input("Saisir un entier : "))
    HammingSeq(n)

if __name__ == "__main__":
    main()