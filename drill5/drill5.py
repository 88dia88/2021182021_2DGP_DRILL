import turtle

def turtlew():
    turtle.setheading(90)
    turtle.forward(50)

    
def turtlea():
    turtle.setheading(180)
    turtle.forward(50)

    
def turtles():
    turtle.setheading(270)
    turtle.forward(50)

    
def turtled():
    turtle.setheading(0)
    turtle.forward(50)

def turtlereset():
    turtle.reset()
    turtle.shape('turtle')

turtlereset()
turtle.shape('turtle')
turtle.onkey(turtlew,'w')
turtle.onkey(turtlea,'a')
turtle.onkey(turtles,'s')
turtle.onkey(turtled,'d')
turtle.onkey(turtlereset,'Escape')

turtle.listen()

