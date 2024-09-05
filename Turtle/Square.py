import turtle as t
t.getscreen()
t.speed('slowest')
t.shape('turtle')
t.pensize(1)
t.pencolor('yellow')


def direc(value):
    t.forward(100)
    t.left(90)
    
for i in range(4):
    direc(90)

#methods
t.exitonclick()
# t.done()
# t.mainloop()