from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        self.createSnake()
        self.head = self.snake[0]
        self.head.color("green")

    def createSnake(self):
        for i in range(0, 60, 20):
            s = Turtle(shape="square")
            s.color("white")
            s.penup()
            s.setx(i * -1)
            self.snake.append(s)

    def grow(self):
        s = Turtle(shape="square")
        s.color("white")
        s.penup()
        s.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        self.snake.append(s)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            newX = self.snake[i - 1].xcor()
            newY = self.snake[i - 1].ycor()
            self.snake[i].goto(newX, newY)
        self.head.forward(20)

    def turnNorth(self):
        if self.head.heading() != 270 and self.head.xcor() != self.snake[1].xcor():
            self.head.setheading(90)

    def turnSouth(self):
        if self.head.heading() != 90 and self.head.xcor() != self.snake[1].xcor():
            self.head.setheading(270)

    def turnEast(self):
        if self.head.heading() != 180 and self.head.ycor() != self.snake[1].ycor():
            self.head.setheading(0)

    def turnWest(self):
        if self.head.heading() != 0 and self.head.ycor() != self.snake[1].ycor():
            self.head.setheading(180)

