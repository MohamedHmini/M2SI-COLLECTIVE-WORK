# -*- coding: cp1252 -*-
import copy

# pour utiliser la fonction deepcopy qui copie une liste dans une autre
FinalListe = []


# la liste qui contienne toutes les listes combinaisons possibles

def Is2Extedable(l,k) :
    i=k
    for i in range(k,NbrDice+1):
        if(l[i]==0) :
            return i
    return -1

def Is3Extedable(l,k) :
    i=k
    for i in range(k,NbrDice+1):
        if(l[i]==1 or l[i]==0) :
            return i
    return -1

def Is4Extedable(l,k) :
    i = k
    for i in range(k, NbrDice + 1):
        if(l[i]==2 or l[i]==1 or l[i] ==0) :
            return i
    return -1


def Is5Extedable(l,k) :
    i = k
    for i in range(k, NbrDice + 1):
        if(l[i]==3 or l[i] ==2 or l[i] == 1 or l[i] == 0) :
            return i
    return -1


def Is6Extedable(l,k) :
    i = k
    for i in range(k, NbrDice + 1):
        if(l[i] == 4 or l[i]==3 or l[i] ==2 or l[i] == 1 or l[i] == 0) :
            return i
    return -1


def f2(liste, k, FinalListe1):  # 'liste' est la liste à étendre et 'k' l'indice en cours
    l1 = copy.deepcopy(liste)
    it = k
    i=k
    last2=k
    first0=NbrDice
    tempListe = []
    if (k < NbrDice):
        for i in range(k+1,NbrDice+1) :
            if(l1[i]==2):
                last2=i
        i=k+1
        while (l1[i]!=0):
            i=i+1
        first0=i
        l1[first0] = 1
        l1[last2] = 1
        tempListe.append(l1)
        it = last2 - 1
        while (it >= k):
            for l in tempListe:
                if(Is2Extedable(l,it)!=-1):
                    f2(l, it, tempListe)
            it = it - 1
        FinalListe1.extend(x for x in tempListe if x not in FinalListe1 )



def f3(liste, k, FinalListe1):
    # 'liste' est la liste à étendre et 'k' l'indice
    l1 = copy.deepcopy(liste)
    it = k
    tempListe = []
    sit=NbrDice
    last3=k
    if (k + 1 <= NbrDice):
        for i in range(k+1,NbrDice+1) :
            if(l1[i]==3):
                last3=i
        sit= Is3Extedable(l1,k)
        l1[last3]=2
        l1[sit]=l1[sit]+1
        tempListe.append(l1)
        i=sit
        if(l1[sit] == 1):
            it=sit-1
        else :
            it=sit
        while (it >= k):
            for l in tempListe:
                if(l[it]==2):
                    if(Is2Extedable(l,it)!=-1):
                        f2(l, it, tempListe)
                elif(l[it]==3):
                    if(Is3Extedable(l,it)!=-1):
                        f3(l, it, tempListe)
            it = it - 1
        FinalListe1.extend(x for x in tempListe if x not in FinalListe1 )






def f4(liste, k, FinalListe1):  # 'liste' est la liste à étendre et 'k' l'indice
    l1 = copy.deepcopy(liste)
    it = k
    tempListe = []
    sit = NbrDice
    last4 = k
    if (k + 1 <= NbrDice):
        for i in range(k + 1, NbrDice + 1):
            if (l1[i] == 4):
                last4 = i
        sit = Is4Extedable(l1, k)
        l1[last4] = 3
        l1[sit] = l1[sit] + 1
        tempListe.append(l1)
        i = sit
        if (l1[sit] == 1):
            it = sit - 1
        else:
            it = sit
        while (it >= k):
            for l in tempListe:
                if (l[it] == 2):
                    if (Is2Extedable(l,it) != -1):
                        f2(l, it, tempListe)
                elif (l[it] == 3):
                    if (Is3Extedable(l,it) != -1):
                        f3(l, it, tempListe)
                elif (l[it] == 4):
                    if (Is4Extedable(l,it) != -1):
                        f4(l, it, tempListe)
            it = it - 1
        FinalListe1.extend(x for x in tempListe if x not in FinalListe1 )


def f5(liste, k, FinalListe1):  # 'liste' est la liste à étendre et 'k' l'indice
    l1 = copy.deepcopy(liste)
    it = k
    tempListe = []
    sit = NbrDice
    last5 = k
    if (k + 1 <= NbrDice):
        for i in range(k + 1, NbrDice + 1):
            if (l1[i] == 5):
                last5 = i
        sit = Is5Extedable(l1, k)
        l1[last5] = 4
        l1[sit] = l1[sit] + 1
        tempListe.append(l1)
        i = sit
        if (l1[sit] == 1):
            it = sit - 1
        else:
            it = sit
        while (it >= k):
            for l in tempListe:
                if (l[it] == 2):
                    if (Is2Extedable(l,it) != -1):
                        f2(l, it, tempListe)
                elif (l[it] == 3):
                    if (Is3Extedable(l,it) != -1):
                        f3(l, it, tempListe)
                elif (l[it] == 4):
                    if (Is4Extedable(l,it) != -1):
                        f4(l, it, tempListe)
                elif (l[it] == 5):
                    if (Is5Extedable(l,it) != -1):
                        f5(l, it, tempListe)
            it = it - 1
        FinalListe1.extend(x for x in tempListe if x not in FinalListe1 )


def f6(liste, k, FinalListe1):  # 'liste' est la liste à étendre et 'k' l'indice
    l1 = copy.deepcopy(liste)
    it = k
    tempListe = []
    sit = NbrDice
    last6 = k
    if (k + 1 <= NbrDice):
        for i in range(k + 1, NbrDice + 1):
            if (l1[i] == 6):
                last6 = i
        sit = Is6Extedable(l1, k)
        l1[last6] = 5
        l1[sit] = l1[sit] + 1
        tempListe.append(l1)
        i = sit
        if (l1[sit] == 1):
            it = sit - 1
        else:
            it = sit
        while (it >= k):
            for l in tempListe:
                if (l[it] == 2):
                    if (Is2Extedable(l,it) != -1):
                        f2(l, it, tempListe)
                elif (l[it] == 3):
                    if (Is3Extedable(l,it) != -1):
                        f3(l, it, tempListe)
                elif (l[it] == 4):
                    if (Is4Extedable(l,it) != -1):
                        f4(l, it, tempListe)
                elif (l[it] == 5):
                    if (Is5Extedable(l,it) != -1):
                        f5(l, it, tempListe)
                elif (l[it] == 6):
                    if (Is6Extedable(l,it) != -1):
                        f6(l, it, tempListe)
            it = it - 1
        FinalListe1.extend(x for x in tempListe if x not in FinalListe1 )







def NumberWithDice(n, NbD):
    x = n / 6
    if (x > NbD - 1):
        print "le nombre ", n, "ne peut etre obtenu a partir de :", NbD, "de Dices"
    else:
        y = n % 6
        liste = []
        if (x > 0):
            for i in range(0, x):
                liste.append(6)
        liste.append(y)
        if (x + 1 <= NbD - 1):
            for j in range(x + 1, NbD):
                liste.append(0)
        FinalListe.append(liste)
        if (y == 2):
            if (Is2Extedable(liste,x) !=-1):
                f2(liste, x, FinalListe)
        elif (y == 3):
            if (Is3Extedable(liste,x) !=-1):
                f3(liste, x, FinalListe)
        elif (y == 4):
            if (Is4Extedable(liste) !=-1):
                f4(liste, x, FinalListe)
        elif (y == 5):
            if (Is5Extedable(liste,x) !=-1):
                f5(liste, x, FinalListe)
        k = x - 1
        while (k >= 0):
            if (Is6Extedable(liste,x) !=-1):
                f6(liste, k, FinalListe)
            k = k - 1
    print "les combinaisons possibles sont : \n"
    for l in FinalListe:
        print l, "\n"


n = input('donner un nombre a traite ')
NbD = input('donner le nombre de Dices ')
NbrDice = NbD - 1
NumberWithDice(n, NbD)









