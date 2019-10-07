from ex5 import getHoraire

print('type in the first horaire !!!')
horaire1 = None
while horaire1 == None:
    horaire1 = getHoraire()

print('type in the second horaire !!!')
horaire2 = None
while horaire2 == None:
    horaire2 = getHoraire()

print "How would you like the input displayed??"
while True:
    print "Hours   : 'H/h'"
    print "Minutes : 'M/m'"
    print "Seconds : 'S/s'"
    choice = raw_input('Answer : ')

    if   choice=='H' or choice=='h':
        print abs(float(horaire2) - horaire1) / 3600
        break
    elif choice=='M' or choice=='m':
        print abs(float(horaire2) - horaire1) / 60
        break
    elif choice=='S' or choice=='s':
        print abs(horaire2 - horaire1)  
        break
    else :
        print 'Bad Input!!!!'
        print 'Choose again!'