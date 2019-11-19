

def multiples(l,m):
    i=0
    temp = l[:]
    while i<len(temp):
        if temp[i]%m!=0:
            temp.pop(i)
        i+=1
    return temp

if __name__ == "__main__":
    l = [2,3,7,6,9,12,4]
    print(multiples(l,3))