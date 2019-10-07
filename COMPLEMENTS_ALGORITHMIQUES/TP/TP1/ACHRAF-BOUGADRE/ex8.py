petit = int(raw_input('first number  : '))
grand = int(raw_input('second number : '))

if grand < petit:
    petit, grand = grand, petit

print 'petit = %d, grand = %d'% (petit, grand)