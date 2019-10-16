''' ce programme lit deux nombre puit il affect le plus petit au variable
<petit> est le plus grand au variable <grand> puis il affiche'''



def main():
    petit = input(" Premier nombre : ")
    grand = input(" Deusieme nombre : ")

    if petit>grand:
        petit,grand=grand,petit
    
    print petit,'est le petit et',grand,'est le grand'




if __name__=="__main__":
    main()
