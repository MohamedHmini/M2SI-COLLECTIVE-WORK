def sommeDiviseurs(n):
    somme = 0
    for i in range(1, n):
        if n % i == 0 :
            somme += i
    else :
        return somme

def parfait(n):
    return (n == sommeDiviseurs(n))

def amis(a, b):
    return (sommeDiviseurs(a) == sommeDiviseurs(b))

if __name__=='__main__':
    while True:
        print('-'*36)
        print('1 - Somme des Diviseurs.')
        print('2 - Teste si un nombre est parfait.')
        print('3 - Teste si a et b sont amis.')
        print('4 - Quit!')
        print('-'*36)
        choix = int(input('Choix : '))
        if choix == 4:
            break
        elif choix == 1:
            n = int(input('Nombre n : '))
            print(sommeDiviseurs(n))
        elif choix == 2:
            n = int(input('Nombre n : '))
            print( '{} est Parfait'.format(n) if parfait(n) else '{} n\'est pas Parfait'.format(n) )
        elif choix == 3:
            a, b = map(int, input('a b : ').split())
            print( '{} et {} sont amis'.format(a, b) if amis(a, b) else '{} et {} ne sont pas amis'.format(a, b) )


