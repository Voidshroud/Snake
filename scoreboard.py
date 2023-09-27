from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(275)
        self.getHighScore()
        self.write(f"Score: {self.score}\t High score: {self.highscore}", False, "center", ("Arial", 12, "bold"))


    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}\t High score: {self.highscore}", False, "center", ("Arial", 12, "bold"))
        
    def getHighScore(self):
        with open("highscore.txt") as file:
            self.highscore = file.read()

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, "center", ("Arial", 12, "bold"))
        
        with open("highscore.txt", "r+") as file:
            if self.score > int(file.read()):
                with open("highscore.txt", "w") as file:
                    file.write(str(self.score))
