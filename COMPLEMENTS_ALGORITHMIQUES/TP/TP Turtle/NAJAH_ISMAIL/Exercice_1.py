
import turtle

def Question2(size):
    i=0
    while i<4:
        turtle.forward(size)
        if i > 0 and i < 3:
            turtle.right(90)
        else:
            turtle.left(90)
        i+=1

def Question3(size,rep):
    i=0
    while i<rep:
        Question2(size)
        i+=1

def Question4(size):
    w = turtle.getscreen().window_width()
    while turtle.pos()[0] < w/2:
        turtle.forward(size)
        if turtle.pos()[1]>0:
            turtle.right(90)
        else:
            turtle.left(90)


def main():
    w,h = 600,500
    turtle.setup(width=w,height=h,startx=None,starty=None)
    turtle.up()
    turtle.setx(-w/2)
    turtle.down()

    size = input("Taille d'un cote : ")
    #rep = input("Repetition : ")
    #Question2(size)
    #Question3(size,rep)
    Question4(size)
    turtle.done()


if __name__ == "__main__":
    main()
