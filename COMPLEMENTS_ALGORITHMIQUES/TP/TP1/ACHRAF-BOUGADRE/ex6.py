from ex5 import getHoraire

print('type in the first horaire !!!')
horaire1 = None
while horaire1 == None:
    horaire1 = getHoraire()

print('type in the second horaire !!!')
horaire2 = None
while horaire2 == None:
    horaire2 = getHoraire()

print abs(horaire2 - horaire1)