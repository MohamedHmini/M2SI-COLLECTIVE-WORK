

# EXERCICE 1 :


def listeElts(l):
    ll = len(l)
    r = set()
    for i in range(0,ll - 1):
        if l[i] not in r:
            for j in range(i + 1,ll):
                if l[i] == l[j]:
                    r.add(l[i])
                    break;

    return r


r = listeElts([1,2,15,44,2,6,15,7,1,44,44])
print("REPEATED : {}".format(r))


def ppcm(a,b):
    i = 1
    j = 1

    while i*a is not j*b:
        if i*a > j*b:
            j += 1
        else:
            i += 1

        pass

    return i*a

print("PPCM : {}".format(ppcm(9,12)))


def sous_liste(l1,l2):
    
    r = []
    yes = True
    # ll1 = len(l1)
    # ll2 = len(l2)

    for e in l1:
        if e not in l2:
            yes = False
            break;

        i = l2.index(e)
        try:
            if r[len(r) - 1] + 1 != i:
                yes = False
                break
            else:
                r.append(i)
        except:
            r.append(i)

    return yes


print("IS SUBLIST? : {}".format(sous_liste([1,2],[5,8,1,2,3,9])))

# intersection sans supprimer les doublons:
def intersection_with_dublicates(l1,l2):
    inter = []

    for i in l1:
        if i in l2:
            inter.append(i)
            l2.pop(l2.index(i))

    return inter
    pass

# intersection sand doublans : 
def intersection_without_dublicates(l1,l2):
    return list(set(l1).intersection(l2))
    pass


print("INTERSECTION SANS DOUBLONS: {}".format(intersection_without_dublicates([1,2,2,3,4,4],[2,2,2,3,4])))
print("INTERSECTION AVEC DOUBLONS: {}".format(intersection_with_dublicates([1,2,2,3,4,4],[2,2,2,3,4])))

def supprimer_doublons(l):
    return list(set(l))

print("SUPPRIMER LES DOUBLONS : {}".format(supprimer_doublons([1,2,2,2,3])))



# EXERCICE 2 : 

d = {
    'r1':{'g1','g2','g3','g4'},
    'r2':{'g1','g5','g3'},
    'r3':{'g1','g2','g3'}
}


def nb_ingredients(d,r):
    return len(d[r])


print("NBR INGREDIENTS : {}".format(nb_ingredients(d,'r2')))


def table_ingredients(d):

    table = {}

    for r,gs in d.items():
        for g in gs:
            try:
                table[g].append(r)
            except:
                table[g] = []
                table[g].append(r)

    return table


print("TABLE INGREDIENTS : {}".format(table_ingredients(d)))


def recette_avec(d,ing):
    table = table_ingredients(d)
    return table[ing]


print("RECETTE AVEC : {}".format(recette_avec(d,'g2')))


def tous_ingredients(d):
    table = table_ingredients(d)
    return list(table.keys())



print("TOUS INGREDIENTS : {}".format(tous_ingredients(d)))



def ingredient_principal(d):
    table = table_ingredients(d)
    counts = [len(rs) for ing,rs in table.items()]
    mx = counts.index(max(counts))
    return list(table.items())[mx][0]


print("INGREDIENT PRINCIPAL : {}".format(ingredient_principal(d)))




def recette_sans(d, ing):
    new_d = {}
    for r,ings in d.items():
        if ing not in ings:
            new_d[r] = ings;

    return new_d


print("RECETTE SANS : {}".format(recette_sans(d,'g5')))