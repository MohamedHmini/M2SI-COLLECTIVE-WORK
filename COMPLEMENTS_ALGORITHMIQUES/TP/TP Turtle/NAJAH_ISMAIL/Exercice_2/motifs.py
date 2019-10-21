
import triangles
import turtle
import random

def polygone(size,numbre):
    angle = 360/numbre
    i=0
    while i<numbre:
        turtle.forward(size)
        turtle.left(angle)
        i+=1

def etoile(size,numbre):
    angle = 360/numbre 
    i=0
    while i<numbre:
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(angle)
        i+=1

def etoile2(size,numbre):
    angle = 360/numbre
    i=0
    while i<numbre:
        triangles.triangle2(size,angle)
        turtle.forward(size)
        i+=1

def pickedShape(op):
    if op == 1:
        return etoile
    if op == 2:
        return etoile2
    if op == 3:
        return polygone
    
def draw(option=1,numbre=5,isRandom=False):
    r=3
    angle=0
    size = 3
    speed = 5
    turtle.up()
    w = turtle.getscreen().window_width()
    h = turtle.getscreen().window_height()
    while abs(turtle.pos()[0]) < w/2 and abs(turtle.pos()[0]) < h/2:
        if angle==180 :
            angle=0
            r+=r*0.6
            turtle.forward(r)
        if angle%30==0:
            turtle.down()
            if isRandom:
                option = random.randint(1,3)
            pickedShape(option)(size,numbre)
            size += size*0.1
            turtle.up()
        turtle.left(speed)
        turtle.forward(r)
        angle+=speed

def Question6():
    shapes = [None,"branches","branches","cotes"]
    print ("Choisir un motif : ")
    print (" 1- etoile type 1")
    print (" 2- etoile type 2")
    print (" 3- Polygone")
    op = int(input("Votre choix : "))
    numbre = int(input("Nombre de "+shapes[op]+" : "))
    draw(op,numbre)


def main():
    turtle.setup(500,500,None,None)
    draw(isRandom=True)
    #Question6()
    turtle.done()

if __name__ == "__main__":
    main()