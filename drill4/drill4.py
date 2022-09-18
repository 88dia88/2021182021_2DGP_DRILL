import turtle

vert = 5

while (vert > 0):
    hori = 5
    while (hori > 0):
        turtle.forward(100);turtle.left(90)
        turtle.forward(100);turtle.left(90)
        turtle.forward(100);turtle.left(90)
        turtle.forward(100);turtle.left(90)
        turtle.forward(100)
        hori = hori - 1
    turtle.right(180);turtle.forward(500)
    turtle.right(90);turtle.forward(100)
    turtle.right(90)
    vert = vert - 1
turtle.exitonclick()
