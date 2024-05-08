from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Day 20 - Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb = ScoreBoard()

game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        sb.score += 1
        food.refresh()
        sb.score_count()
        snake.extend()

    for snake_body in snake.turtles[1:]:
        if snake.head.distance(snake_body) < 10:
            sb.high_score_count()
            snake.reset_snake()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        sb.high_score_count()
        snake.reset_snake()

screen.exitonclick()
