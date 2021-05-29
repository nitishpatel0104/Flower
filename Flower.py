import turtle

def draw_diamond(some_turtle):
    some_turtle.shape ("turtle")
    some_turtle.speed (15)
    some_turtle.color ("blue")
    for i in range (1,3):
        some_turtle.fd (50)
        some_turtle.rt (30)
        some_turtle.fd (50)
        some_turtle.rt (150)

def draw_art ():
    window = turtle.Screen ()
    window.bgcolor ("white")
    ken = turtle.Turtle ()
    ken.rt (90)
    for i in range (1, 73):
        draw_diamond (ken)
        ken.rt (5)
    ken.fd (150)
    window.exitonclick()

draw_art()
