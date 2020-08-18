import turtle

BLA = turtle.Turtle()

def line(x1,y1,x2,y2):
    
    xs = 0
    ys = 0
    if x1<x2:
        xs = 1

    else:
        xs = -1   

    if y1<y2:
        ys = 1

    else:
        ys = -1      

    x = x1
    y = y1 
    BLA.penup()
    BLA.goto(x,y)
    BLA.pendown()
    dx = x2-x1
    dy = y2-y1

    if abs(dy)<abs(dx):
        p0 = 2*dy-dx

        while abs(x) < abs(x2):
            if p0<0:
                x = x+1*xs
                BLA.goto(x,y)
                p0 = p0+2*dy
                print(x,y)

            else:
                x = x+1*xs
                y = y+1*ys
                p0 = p0+2*dy-2*dx
                BLA.goto(x,y)
                print(x,y)


    elif abs(dx)<abs(dy):
        p0 = 2*dx-dy

        while abs(y)<abs(y2):
            if p0<0:
                print(xs)

                y = y+1*ys
                BLA.goto(x,y)
                p0 = p0+2*dx
                print(x,y)


            else:
                x = x+1*xs
                y = y+1*ys
                p0 = p0+2*dx-2*dy
                BLA.goto(x,y)
                print(x,y)

                    


line(-10,20,87,160)                    
turtle.done()