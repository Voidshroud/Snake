from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.title("Snake")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()

screen.onkeyrelease(snake.turnNorth, "w")
screen.onkeyrelease(snake.turnSouth, "s")
screen.onkeyrelease(snake.turnEast, "d")
screen.onkeyrelease(snake.turnWest, "a")

GameOn = True

while GameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Eating food
    if snake.head.distance(food) < 20:
        food.respawn()
        snake.grow()

    # Hitting the tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            GameOn = False

    # Passing through the edge
    if snake.head.xcor() > 280:
        snake.head.setx(-280)
    if snake.head.xcor() < -280:
        snake.head.setx(280)
    if snake.head.ycor() > 280:
        snake.head.sety(-280)
    if snake.head.ycor() < -280:
        snake.head.sety(280)

screen.exitonclick()
