def dist(a, b):
    return ( (b[0] - a[0])**2 + (b[1] - a[1])**2 ) ** 0.5

if __name__=='__main__':
    x, y = input('(x1, y1) = ')
    a = (x, y)

    x, y = input('(x2, y2) = ')
    b = (x, y)

    print 'La distance entre les deux points est de %d'%( dist(a, b) )