import ex12_1 

def dans_cercle(point, cercle):
    distance = ex12_1.dist(point, cercle['center'])
    if distance <= cercle['rayon']:
        return True
    else :
        return False



if __name__=='__main__':
    x, y = input('Entrer les coordonnees du centre du cercle : ')
    rayon = int(raw_input('Entrer le rayon du cercle : '))
    cercle = { 'center':     (x,y),     'rayon': rayon}    

    x, y = input('Entrer les coordonnees du point : ')
    point=(x, y)

    if dans_cercle(point, cercle) :
        print 'Le point est a l\'interieur du cercle.'
    else :
        print 'Le point est a l\'exterieur du cercle.'

