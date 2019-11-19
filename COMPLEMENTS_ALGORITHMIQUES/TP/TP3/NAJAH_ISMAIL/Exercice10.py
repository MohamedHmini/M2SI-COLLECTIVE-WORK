

def drapeau(l):
    i=0
    while i<len(l)-1:
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            i=0
        i+=1
    return l

print(drapeau([0,1,2,0,0,2,2,2,0,1,1,0,1,2,0,2,1]))