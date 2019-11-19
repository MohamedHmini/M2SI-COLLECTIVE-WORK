

def appartient(l,elt):
    ''' appartient : (list,element) : boolean
    cette fonction test si l'element aparaitre dans 
    la list'''
    i=0
    while i<len(l):
        if l[i]==elt:
            return True
        i+=1
    return False

def appartient2(l,elt):
    return elt in l

if __name__ == "__main__":
    l = [1,2,3,6,4,8,7]
    print(appartient(l,5))
    print(appartient2(l,2))