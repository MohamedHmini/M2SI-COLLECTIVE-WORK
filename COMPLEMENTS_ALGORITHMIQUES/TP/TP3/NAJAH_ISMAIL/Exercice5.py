

def Somme(l):
    s,i=0,0
    while i<len(l):
        s+=l[i]
        i+=1
    return s

def Somme2(l):
    return sum(l)

if __name__ == "__main__":
    l = [1,2,2,3,18,5]
    print(Somme(l))
    print(Somme2(l))