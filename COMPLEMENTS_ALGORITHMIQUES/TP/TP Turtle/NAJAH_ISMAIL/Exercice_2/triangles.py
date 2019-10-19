
import turtle

def triangle(size):
    #turtle.left(60)
    for i in range(3):
        turtle.forward(size)
        turtle.right(120)

def triangle2(size,angle):
    turtle.left(angle)
    triangle(size)


def main():
    turtle.setup(500,500,None,None)
    triangle(60)
    turtle.done()

if __name__ == "__main__":
    main()