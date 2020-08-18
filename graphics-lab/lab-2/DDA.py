import turtle

DDA = turtle.Turtle()




def line(x1,y1,x2,y2):
    x = x1
    y = y1
    DDA.penup()
    DDA.goto(x,y)
    DDA.pendown()
    i = 0
    dx = x2-x1
    dy = y2-y1
    if abs(dx) > abs(dy):
         steps = abs(dx)

    else:
         steps = abs(dy)

    x_incerement = dx/float(steps)
    y_incerement = dy/float(steps)

    for i in range(steps):
        x = x+ x_incerement
        y = y+ y_incerement
        print(round(x),round(y))

        DDA.goto(x,y)

line(-3,1,-78,-275)


turtle.done()