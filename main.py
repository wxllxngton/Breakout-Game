from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
from blocks import Block
import time

start_game = time.time()

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Breakout')
screen.tracer(0)

ball = Ball()
paddle = Paddle((0,-250))
blocks = Block()
scoreboard = Scoreboard()

# Moves the paddle
screen.listen()
screen.onkey(key="Left",fun=paddle.go_left)
screen.onkey(key="Right",fun=paddle.go_right)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collsion with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collsion with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -225:
        ball.bounce_y()

    # Detect when paddle misses
    if ball.ycor() < -280:
        ball.reset_position()

    # Detect collsion between walls and paddle
    if paddle.xcor() < -340: # Left wall
        paddle.backward(-10)

    if paddle.xcor() > 340: # Right wall
        paddle.backward(10)

    # Detect collsion with block
    for block in blocks.all_blocks:
        if ball.distance(block) < 30:
            block.goto(-1000,1000)
            scoreboard.increase_score()
            ball.bounce_y()

    # Win Game
    if scoreboard.score == 180:
        end_game = round(float(time.time() - start_game),2)
        scoreboard.victory(time=end_game)
        game_is_on = False


screen.exitonclick()
