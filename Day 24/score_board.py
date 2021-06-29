from turtle import Turtle

FONT=("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("data.txt",mode="r") as data:
            self.high_score=int(data.read())

        self.goto(x=0, y=268)
        self.score=0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score  =  {self.score}  High Score = {self.high_score}", False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score=0
        self.score_update()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.score_update()



