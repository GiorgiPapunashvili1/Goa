from turtle import *
#we want to paint a house


speed(3)
color("blue")
begin_fill()
width(7) 
forward(200)
left(90)
     
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(75)
left(90)
end_fill()
#end of square

#drawing a door

color("yellow")
begin_fill()
forward(100)
right(90)

forward(50)
right(90)

forward(100)
end_fill()


color("blue")
begin_fill()

right(90)
forward(125)

left(180)
end_fill()
penup()
goto(200, 200)
pendown()
begin_fill()
right(180 + 60)
end_fill()



color("red")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(25, 150)
pendown()

left(30)

color("cyan")

begin_fill()

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

end_fill()


penup()
goto(135, 150)
pendown()



begin_fill()
forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)
end_fill()









exitonclick()