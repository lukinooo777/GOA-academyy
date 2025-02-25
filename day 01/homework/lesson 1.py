print(5)
print("5")
print(5+ int("5"))
print("luka khurtsidze aris "  +  "5" +  "wlis")
#we want to paint a house
from turtle import *
# step 1: draw a square

speed(30)
width(7)
color("red")


forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("black")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# we want to draw a window

left(30)
forward(90)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(25)
left(90)
forward(60)
penup()
goto(200,200)
pendown()
forward(90)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
left(180)
forward(25)
left(90)
forward(60)
right(90)
forward(25)
right(90)
forward(30)
right(90)
forward(50)







exitonclick()