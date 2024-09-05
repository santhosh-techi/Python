import turtle as t
t.getscreen()
# t.pencolor('red')
# t.fillcolor('green')
t.color('red','green')
t.begin_fill()
t.circle(100)
t.end_fill()
t.rt(90)
t.penup()
t.isdown()
t.forward(100)
t.pendown()
t.color('black','orange')
t.begin_fill()
t.circle(50)
t.end_fill()
t.rt(90)
t.begin_fill()
t.circle(50)
t.end_fill()

#to get the position of turtle we have position() and pos()
print(t.position())
print(t.pos())

#to change the position we have goto() method

t.goto(-100,-100)



t.exitonclick()