import turtle as trtl
import random

spiral = trtl.Turtle()
spiral.speed(-1)
spiral.penup()
spiral.shape("circle")

#Default spiral function
def regular_spiral(x, y, size, direction):
  for spiral_space in range(10,size): 
    spiral.goto(x,y)
    if direction == "left":
      spiral.left(5)
    else:
      spiral.right(5)
    spiral.forward(10+spiral_space*0.9)
    spiral.pendown()
    spiral.stamp()
    spiral.penup()

#background
spiral.goto(0,-5000)
spiral.fillcolor("dark blue")
spiral.begin_fill()
spiral.circle(5000,360,4)
spiral.end_fill()

#Spiral #1
spiral.color("light blue")
spiral.pensize(20)

regular_spiral(-270,150,175, "left")

spiral.setheading(180)
spiral.pendown()
spiral.forward(400)
spiral.penup()


#spiral 2
spiral.color("cyan")
spiral.setheading(0)
spiral.goto(-230,-40)
spiral.pendown()
spiral.circle(180,-120)

spiral.penup()
spiral.goto(-230,-40)
spiral.setheading(0)
spiral.pendown()
spiral.forward(750)
spiral.setheading(180)
spiral.circle(100,-180)
spiral.penup()

#spiral 3

spiral.setheading(270)
for spiral_space in range(100,280): 
  spiral.goto(520,-142)
  spiral.left(3)
  spiral.forward(10-spiral_space*0.4)
  spiral.pendown()
  spiral.stamp()

  spiral.penup()

#Extra Spirals in random places
spiral.color("skyblue")
regular_spiral(random.randint(200,400), random.randint(150,225), random.randint(120,280), "right")


spiral.color("cornflowerblue")
regular_spiral(random.randint(-400,-300), random.randint(-200,-150), random.randint(120,240), "left")

wn = trtl.Screen()
wn.mainloop()