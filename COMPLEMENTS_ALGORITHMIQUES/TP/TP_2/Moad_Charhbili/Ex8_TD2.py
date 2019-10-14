def main():
    a = int(input('Saisir un entier : '))
    i=1
    while a > 0:
        a-=1
        print(a*' '+i*'*')
        i+=2

if __name__ == '__main__':
    main()