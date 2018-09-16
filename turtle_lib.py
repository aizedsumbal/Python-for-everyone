import turtle

pen=turtles.Turtle()

pen.speed(0)
def make_triangle():
    for i in range(3):
        pen.forward(100)
        pen.left(120)
def series_triangle():
    for i in range(3):
##        make_triangle()
        pen.forward(100)

def make_square():
    for i in range(4):
        if(i==0 ):
            pen.pencolor('yellow')
        elif(i==1 ):
            pen.pencolor('black')
        elif(i==2 ):
            pen.pencolor('blue')
        elif(i==3 ):
            pen.pencolor('red')

        pen.forward(100)
        pen.left(90)

for i in range(0,360,1):
    pen.left(i)
    make_square();
    pen.home()



window=turtle.Screen()
window.exitonclick()
