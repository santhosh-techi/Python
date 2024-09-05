import turtle as t
#get screnn
screen=t.getscreen()
#colour of turtle
t.color('black')

#creating method
def shape():
    t.forward(100)
    t.left(45)

for i in range(8):
    shape()
t.exitonclick()
