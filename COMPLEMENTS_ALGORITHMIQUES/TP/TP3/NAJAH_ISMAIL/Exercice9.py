


def derivee(poly):
    d = poly[1:]
    i,j=1,0
    while i<len(poly):
        d[j] = poly[i]*i
        i+=1
        j+=1
    return d

def somme(poly1,poly2):
    s = poly1[:] if len(poly1)>len(poly2) else poly2[:]
    i,j=0,0
    while i<len(poly1) and j<len(poly2):
        s[i] = poly1[i]+poly2[j]
        i+=1
        j+=1
    return s

def multiplication(pol1,pol2):
    result = [0]*(len(pol1)+len(pol2)-1)
    i=0
    while i<len(pol1):
        j=0
        if pol1[i]==0:
            i+=1
            continue
        while j<len(pol2):
            result[i+j] += pol1[i]*pol2[j]
            j+=1
        i+=1 
    return result

if __name__ == "__main__":
    print(derivee([1,0,5,3]))
    print(somme([0,0,5],[5,2]))
    print(multiplication([1,0,5,3],[1,1,5]))