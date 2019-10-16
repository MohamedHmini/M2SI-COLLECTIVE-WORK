# -*- coding: cp1256 -*-
'''ce programme demande a l'utilsateur de saisir deus horair
 puit inl retourne le temps entre entre ces deux horaires
 en nombre de secondes'''

from checkLib import checkInput as get


    

def main():
    print '---- Premier horaire ----'
    h1 = get(' Heures : ',0,24)
    m1 = get(' Minutes : ',0,60)
    s1 = get(' Secondes : ',0,60)

    print '---- Deuxiéme horaire ----'
    h2 = get(' Heures : ',0,24)
    m2 = get(' Minutes : ',0,60)
    s2 = get(' Secondes : ',0,60)

    diff = abs(getSecondes(h1,m1,s1) - getSecondes(h2,m2,s2))
    heure,minutes,secondes = secondes_to_HMS(diff)
    print 'le temp entre ces deux horaire en secondes est ',diff
    print 'equivalent',heure,'H',minutes,'min',secondes,'s'

def getSecondes(heurs,minutes,secondes):
    return heurs*3600 + minutes*60 + secondes

def secondes_to_HMS(secondes):
    return secondes/3600,(secondes%3600)/60,secondes%60

if __name__=="__main__":
    main()
