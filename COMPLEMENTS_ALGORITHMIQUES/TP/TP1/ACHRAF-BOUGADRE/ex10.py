choix = raw_input('Ski avec ou sans chaussures (SANS/AVEC) : ').lower()

avec = ( (15, 10), (90, 60) )
sans = ( (10, 8), (60, 48) )
a = None # journee ou semaine
b = None #enfant ou adulte
price_to_pay = 0 # prix a payer

if choix == 'avec':
    a = raw_input('A la journee ou A la semaine (j/s) : ').lower()
    if a == 'j':
        b = raw_input('Pour enfant ou pour adulte (E/A) : ').lower()
        if b == 'e':
            price_to_pay += 10
        elif b == 'a':
            price_to_pay += 15

    elif a == 's':
        b = raw_input('Pour enfant ou pour adulte (E/A) : ').lower()
        if b == 'e':
            price_to_pay += 60
        elif b == 'a':
            price_to_pay += 90

elif choix == 'sans':
    a = raw_input('A la journee ou A la semaine (j/s) : ').lower()
    if a == 'j':
        b = raw_input('Pour enfant ou pour adulte (E/A) : ').lower()
        if b == 'e':
            price_to_pay += 8
        elif b == 'a':
            price_to_pay += 10

    elif a == 's':
        b = raw_input('Pour enfant ou pour adulte (E/A) : ').lower()
        if b == 'e':
            price_to_pay += 48
        elif b == 'a':
            price_to_pay += 60


baton = raw_input('Ski avec ou sans baton (SANS/AVEC) : ').lower()

a = None # journee ou semaine
if baton == 'avec':
    c = raw_input('A la journee ou A la semaine (j/s) : ').lower()
    if c == 'j':
        price_to_pay += 3
    elif c == 's':
        price_to_pay += 18

print "the price to pay is %d" % price_to_pay