import turtle as t
color_list=['red','blue','orange','green','pink','yellow']
#defining angle
angle=360
color_value=0
t.pensize(2)
for i in range(3,9): #3,4,5,6,7,8
    ang=angle//i
    t.penup()
    cl=color_list[color_value]
    t.begin_fill()
    for i in range(i):
        t.color(cl)
        t.forward(50)
        t.pendown()
        t.left(ang)
    t.end_fill()
    color_value+=1


t.exitonclick()