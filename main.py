from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("snack game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    screen.update()

    game_running = True

    eat = False
    while game_running:
        screen.update()
        time.sleep(0.1)

        snake.move(eat)
        if snake.head.distance(food) < 18:
            food.set_position()
            eat = True
            scoreboard.add_score()
        else:
            eat = False

        # check wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_running = False
            scoreboard.game_over()

        # check body
        for snake_body in snake.block_list[1:]:
            if snake.head.distance(snake_body) < 10:
                game_running = False
                scoreboard.game_over()

    screen.exitonclick()
