from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time
from tkinter import messagebox

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Michael's Snake Game")
screen.tracer(0)

# Creating starting snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Start game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        screen.update()
        scoreboard.game_over()
        yes_or_no = messagebox.askyesno(message="Do you want to play again?")
        if yes_or_no:
            game_is_on = True
            snake.reset_snake()
            scoreboard.update_highscore()
            scoreboard.reset_board()
        else:
            game_is_on = False
            scoreboard.update_highscore()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            screen.update()
            scoreboard.game_over()
            yes_or_no = messagebox.askyesno(message="Do you want to play again?")
            if yes_or_no:
                game_is_on = True
                snake.reset_snake()
                scoreboard.update_highscore()
                scoreboard.reset_board()
            else:
                game_is_on = False
                scoreboard.update_highscore()

    screen.listen()

    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)


screen.mainloop()