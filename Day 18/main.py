import random
import turtle as t
from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
timmy.color("PaleGreen4")
timmy.shapesize(2,2,1)



"""DRAW SHAPES
    def draw_shape(side,angle):
    for number in range(side):
        timmy.forward(100)
        timmy.right(angle)

def sides():
    for x in range(3,10):
        timmy.pencolor(random.choice(colour))
        angle=360/x
        draw_shape(x,angle)
sides()
"""
"""DRAW A DASHED LINE:
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()"""


"""RANDOM WALK
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random_color())
    timmy.pencolor(random_color())
    walk=[0,90,180,270]
    timmy.forward(20)
    move=random.choice(walk)
    timmy.setheading(move)"""
"""  FINAL PROBLEM
"""
"""t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
timmy.speed("fastest")
def draw_spirograph(size_of_gap):
    timmy.shape("arrow")
    for _ in range(360//size_of_gap):
        timmy.color(random_color())
        timmy.pencolor(random_color())
        timmy.circle(100)
        current_heading=timmy.heading()
        timmy.setheading(current_heading+size_of_gap)

draw_spirograph(5)
"""
"""import colorgram
rgb_colors=[]
colors=colorgram.extract('image.jpg',30)
for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)"""


