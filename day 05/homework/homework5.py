#მას ეს დავალება ცოტა გაქცევაზე მაქვს დაზერილი დრო არ მქონა მთელი ბოლო 3 დღე და ბოდიშს გიხდით


from turtle import *

#drawing 3 houses


bgcolor("green")




speed(0)
width(5)




color("black")






penup()
goto(-300,200)
pendown()

begin_fill()

forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
left(45)
forward(125)
right(90)
forward(125)

end_fill()

penup()
goto(-100,-100)
pendown()

begin_fill()

left(45)
forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
left(45)
forward(125)
right(90)
forward(125)

end_fill()


penup()
goto(100,200)
pendown()
left(45)
forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
left(45)
forward(125)
right(90)
forward(125)

end_fill()

width(400)
penup()
goto(-500,500)
pendown()
color("cyan")
left(45)
forward(1000)
color("black")

width(5)

penup()
goto(100,200)
pendown()

begin_fill()

forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
forward(180)
right(90)
left(45)
forward(125)
right(90)
forward(125)

end_fill()

left(135)
penup()
forward(200)
pendown()
color("yellow")

begin_fill()

forward(100)
right(90)
forward(200)
right(90)
forward(300)
right(90)
forward(200)
end_fill()







exitonclick() 