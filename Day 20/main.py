import time
from turtle import Turtle,Screen
from snake import Snake

snake=Snake()
screen=Screen()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
screen.tracer(0)

is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()


screen.exitonclick()