from turtle import Turtle,Screen
tim=Turtle()
tim.speed("fastest")
def w():
    tim.forward(10)
def s():
    tim.backward(10)
def a():
    tim.left(10)

def d():
    tim.right(10)
def c():
    tim.clear()
    tim.home()


screen=Screen()
screen.onkey(w,"w")
screen.onkey(s,"s")
screen.onkey(a,"a")
screen.onkey(d,"d")
screen.onkey(c,"c")
screen.listen()


screen.exitonclick()
