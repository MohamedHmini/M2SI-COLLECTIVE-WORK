def main():
    l=-1
    while l!=0:
        l=int(input("1)Skis avec chaussures :\n 2)Skis sans chaussures \n 3)les batons : 3 euros par jour et 18 euros en forfait semaine \n 0)Exit"))
        if l==1:
            c = int(input("1)a la Journee :\n 2)Forfait semaine \n 0)Retour"))
            if c==1:
                b = int(input("Combiens des jours ?"))
                p = int(input("1)Adulte : 15  :\n 2)Enfant : 10 \n 0)Retour"))
                if p==1:
                    print("Vous devez payer ", b*15," Euros")
                    l = 0
                if p==2:
                    print("Vous devez payer ", b*10," Euros")
                    l = 0
            if c==2:
                b = int(input("Combiens des semaines ?"))
                p = int(input("1)Adulte : 90  :\n 2)Enfant : 60 \n 0)Retour"))
                if p==1:
                    print("Vous devez payer ", b*90," Euros")
                    l=0
                if p==2:
                    print("Vous devez payer ", b*60," Euros")
                    l = 0
        if l==2:
            c = int(input("1)a la Journee :\n 2)Forfait semaine \n 0)Retour"))
            if c==1:
                b = int(input("Combiens des jours ?"))
                p = int(input("1)Adulte : 10  \n 2)Enfant : 8 \n 0)Retour"))
                if p==1:
                    print("Vous devez payer ", b*10," Euros")
                    l = 0
                if p==2:
                    print("Vous devez payer ", b*8," Euros")
                    l = 0
            if c==2:
                b = int(input("Combiens des semaines ?"))
                p = int(input("1)Adulte : 60 \n 2)Enfant : 48 \n 0)Retour"))
                if p==1:
                    print("Vous devez payer ", b*60," Euros")
                    l = 0
                if p==2:
                    print("Vous devez payer ", b*48," Euros")
                    l = 0
            if l==3:
                p = int(input("1)par jour   \n 2)Forfait Semaine\n 0)Retour"))
                if p==1:
                    b=int(input("Combiens des jours ?"))
                    print("Vous devez payez : ",b*3)
                    l = 0
                if p==2:
                    b = int(input("Combiens des semaines ?"))
                    print("Vous devez payez : ", b * 18)
                    l = 0

if __name__=="__main__":
    main()