
def Population(initSet , months):
    adults = []
    i=0
    while i<initSet:
        adults.append(12)
        i+=1
    i = 6
    while i<=months:
        j = 0
        end = len(adults)
        while j<end:
            adults[j]+=6
            if adults[j]>12 and adults[j]<=48:
                adults.append(0)
                adults.append(0)

            #elif adults[j]==48:
                #adults.pop(j)
            j+=1
        i+=6
    return adults

def lapinAdulte(initSet , months):
    s=0
    for i in Population(initSet,months):
        if i >=12:
            s+=1
    return s*2

def lapinPopulation(initSet,populationNumber):
    i=0
    months = 0
    while i<populationNumber:
        months+=6
        i = len(Population(initSet,months)*2)
    return months

if __name__ == "__main__":
    print(len(Population(1,36))*2)