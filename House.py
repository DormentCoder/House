# House
# by E I Dimbleby
# 14/07/2021

# In order to use turtle, we import the turtle library
import turtle

OFFSET = -100

turtle.speed(1)
turtle.penup()
turtle.goto(OFFSET,OFFSET)

# Draw the house :-
turtle.goto(OFFSET,OFFSET)
turtle.fillcolor("Yellow")
turtle.begin_fill()
turtle.pendown()
for i in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

# Draw the roof :-
turtle.goto(OFFSET,OFFSET + 150)
turtle.fillcolor("Red")
turtle.begin_fill()
turtle.pendown()
turtle.forward(200)
turtle.left(120)
turtle.forward(80)
turtle.left(60)
turtle.forward(120)
turtle.left(60)
turtle.forward(80)
turtle.left(120)
turtle.end_fill()
turtle.penup()

# Draw the door :-
turtle.goto(OFFSET + 30, OFFSET)
turtle.hideturtle()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.pendown()
for i in range(0,2):
  turtle.forward(60)
  turtle.left(90)
  turtle.forward(110)
  turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(OFFSET + 35, OFFSET + 55)
turtle.fillcolor("Black")
turtle.begin_fill()
turtle.circle(4)
turtle.end_fill()

# Draw the window :-
turtle.goto(OFFSET + 120, OFFSET + 50)
turtle.fillcolor("Light Blue")
turtle.begin_fill()
turtle.pendown()
for i in range(0,2):
  turtle.forward(60)
  turtle.left(90)
  turtle.forward(60)
  turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(OFFSET + 120, OFFSET + 80)
turtle.pendown()
turtle.forward(60)
turtle.penup()
turtle.goto(OFFSET + 150, OFFSET + 50)
turtle.left(90)
turtle.pendown()
turtle.forward(60)

turtle.hideturtle()

turtle.penup