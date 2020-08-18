import turtle

sun = turtle.Turtle()

sun.fillcolor('red')

sun.begin_fill()
sun.right(100)
sun.circle(50,200)
sun.up()

sun.goto(0,0)
sun.setheading(0)
sun.right(80)
sun.pendown()
sun.circle(50,160)
sun.right(63)
sun.end_fill()



# for i in range(6):
#     sun.left(120)
#     sun.forward(7)

#     sun.right(150)
#     sun.forward(7)







turtle.done()