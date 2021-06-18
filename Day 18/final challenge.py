import random
import turtle as t
from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("arrow")
timmy.color("PaleGreen4")
timmy.shapesize(2,2,1)
timmy.penup()
timmy.hideturtle()
colors = [(125, 98, 61), (30, 22, 12), (77, 77, 133), (107, 91, 105), (23, 47, 157), (158, 129, 81), (182, 154, 113),
          (96, 71, 20), (18, 21, 55), (89, 103, 190), (240, 228, 191), (22, 17, 20), (134, 151, 176), (223, 199, 136),
          (146, 160, 153), (2, 4, 3), (149, 136, 144), (228, 232, 240), (142, 121, 116), (242, 246, 245),
          (98, 114, 108),
          (136, 120, 133), (72, 57, 75), (79, 58, 51), (114, 135, 128), (234, 228, 232), (177, 183, 217),
          (100, 141, 145),
          (171, 199, 203), (180, 198, 192)]
t.colormode(255)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def spot_painting(size):
    for times in range(1,size+1):
        clr = random.choice(colors)
        timmy.dot(20, clr)
        timmy.forward(50)
        if times % 10==0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)



spot_painting(100)


screen = Screen()
screen.exitonclick()