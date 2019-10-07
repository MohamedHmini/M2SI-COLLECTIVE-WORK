from ex12_2 import dans_cercle 

def dans_intersection(point, cercle1, cercle2):
    if dans_cercle(point, cercle1) and dans_cercle(point, cercle2):
        return True
    return False



if __name__=='__main__':
    cercles = []
    for i in range(1, 3):
        x, y = input('Entrer les coordonnees du centre du cercle %d : ' % (i))
        rayon = int(raw_input('Entrer le rayon du cercle %d : ' %(i)))
        print "\n"

        cercle = { 'center':     (x,y),     'rayon': rayon}    
        
        cercles.append(cercle)

    x, y = input('Entrer les coordonnees du point : ')
    point=(x, y)
    print "\n"

    if dans_intersection(point, *cercles) :
        print 'Le point est dans l\'intersection des deux cercles.'
    else :
        print 'Le point n\'est pas dans l\'intersection des deux cercles.'


    