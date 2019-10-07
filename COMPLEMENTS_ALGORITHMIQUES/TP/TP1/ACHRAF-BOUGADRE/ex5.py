def getHoraire():
    horaire = [int(element) for element in raw_input('[heure:min:sec] : ').split(':')]

    def testIfInputIsRight():
        return reduce( 
                (lambda a,b: a and b)  
                , map(  
                        (lambda x: not(x >= 60 or x < 0) )
                        , horaire 
                    ) 
            )

    if len(horaire) != 3 or not testIfInputIsRight():
        print 'bad input'
        return None
    else:
        return int(horaire[0]) * 60 * 60 + int(horaire[1]) * 60 + int(horaire[2]) 
        
if __name__=='__main__':
    horaireInSec = getHoraire()
    if horaireInSec:
        print horaireInSec 