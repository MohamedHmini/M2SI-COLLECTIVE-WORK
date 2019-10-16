# -*- coding: cp1256 -*-
# ce programme demande a l'utillisateur de saisir un horaire
# exprimé en heur,minutes,secondes et retourn cette durée en nombre
# secondes depuit minuit

from checkLib import checkInput as get

heur = get(' Heures : ',0,24)
minutes = get(' Minutes : ',0,60)
secondes = get(' Secondes : ',0,60)

print ' le nombre de secondes depuit minuit est',heur*3600+minutes*60+secondes,'s'
