import turtle


flag = turtle.Turtle()

def outline():
    flag.up()
    flag.goto(0,-130)
    flag.down()

    flag.pensize(3.5)
    flag.color('#00008B','#8B1919')
    flag.begin_fill()
    
    flag.goto(0,100)  
    flag.goto(133.5,-40)
    flag.penup()
    flag.goto(40,10)
    flag.pendown()
    flag.penup()
    flag.goto(133.5,-40)
    flag.pendown()
    flag.goto(40,-40)
    flag.goto(133.5,-130)
    flag.goto(0,-130)

    flag.end_fill()


def sun():

    flag.penup()
    flag.goto(53,-90)
    flag.pendown()

    flag.pensize(1)
    flag.pencolor('white')
    flag.fillcolor('white')
    flag.begin_fill()

    for i in range(12):
     flag.left(30)
     flag.forward(10)
     flag.left(120)
     flag.forward(10)
     flag.right(120)
   
 
    flag.end_fill()    


def moon():
    flag.pensize(1)
    flag.penup()
    flag.goto(10,10)

    flag.pendown()
    
    flag.pencolor('white')
    flag.fillcolor('white')
    

    flag.begin_fill()
    flag.right(100)
    flag.circle(25,360)
    flag.end_fill()
    flag.penup()
    flag.goto(10,10)
    flag.setheading(0)
    flag.right(70)
     
    flag.pencolor("#8B1919") 
    flag.fillcolor("#8B1919")
    flag.begin_fill()
    flag.pendown()
    flag.circle(25,360)
    flag.end_fill()

    flag.penup()
    flag.goto(10,10)
    flag.setheading(0)
    flag.right(100)
    flag.circle(25,65)
    
    flag.pencolor('white')
    flag.fillcolor('white')
    flag.begin_fill()

    flag.pendown()
    flag.left(90)
    flag.forward(12)
    

    for i in range(9):
        flag.left(120)
        flag.forward(7)

        flag.right(150)
        flag.forward(7)
        
    flag.end_fill()    




outline()

sun()

moon()


turtle.done()
