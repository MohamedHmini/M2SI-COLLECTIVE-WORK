
from checkLib import checkInput as get

def menu(menuList):
    i=1
    for option in menuList:
        print(str(i),')',option)
        i+=1
    
    o = int(get("choisi une option : ",1,len(menuList)+1))
    return (menuList[o-1],o)

def calculPrix(p):
    prix=0
    if p[0] == 1:
        if p[1]==1:
            if p[2]==1:
                prix = 90
            else:
                prix = 15
        else:
            if p[2]==1:
                prix = 60
            else:
                prix = 10
    else:
        if p[1]==1:
            if p[2]==1:
                prix = 60
            else:
                prix = 10
        else:
            if p[2]==1:
                prix = 48
            else:
                prix = 8
    if p[3]==1:
        prix += 18
    else:
        prix += 3
    return prix




def main():
    list1="Skis avec chaussures.;Skis sans chaussures.".split(';')
    list2=["Adult","Enfant"]
    list3=["Semaine","Journee"]
    prixTotal = []
    fo = menu(list1)
    print(fo[0])
    prixTotal.append(fo[1])
    So = menu(list2)
    prixTotal.append(So[1])
    print(fo[0],'pour un',So[0])
    To = menu(list3)
    prixTotal.append(To[1])
    print('les batons pour :')
    o = menu(list3)
    prixTotal.append(o[1])
    print('location de'+fo[0],end=' ')
    print('pour un'+So[0],end=' ')
    print('pour une'+To[0],end=' ')
    print('avec les batons pour'+o[0])
    p = calculPrix(prixTotal)
    print('\nPrix est :'+str(p))

if __name__ == "__main__":
    main()