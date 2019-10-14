

def sommeDiviseurs(n):
    ''' sommeDiviseurs : (int) -> int
        retourn la somme des diviseurs du n'''
    div = [x for x in range(1,n/2 + 1) if n%x==0]
    return sum(div)

def parfait(n):
    if n==sommeDiviseurs(n):
        print n,"est parfait."

def amis(n,p):
    if n==sommeDiviseurs(p) and p==sommeDiviseurs(n):
        print n,"et",p,"son des amis."
    else:
        print n,"et",p,"ne son pas des amis."
        

def main():
    print "Choisissez un test :"
    print " 1- un entier Parfait"
    print " 2- deux entier amis"
    op = input("votre choix: ")
    while op>2 or op<1:
        op = input("Erorr!! votre choix: ")
    n = input(" Saisir la valeur n : ")
    if op==1:
        parfait(n)
    else:
        p = input(" Saisir le deuxeme nombre : ")
        amis(n,p)
    

if __name__ == "__main__":
    main()