import turtle
import time

velocities = []

# Set up the screen
window = turtle.Screen()
window.title("Gravity Sim")
window.bgcolor("black")
window.setup(width=1000, height=800)
window.tracer(0)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(-450, 350)
ball.pendown()

# Initial velocity and gravity
velocity = 0
gravity = 0.981
horizontal_velocity = 3

frame_rate = 240
frame_delay = 1 / frame_rate

# Main game loop
while True:
    # Update the velocity
    velocity -= gravity

    # Update the position of the ball
    ball.sety(ball.ycor() + velocity)
    ball.setx(ball.xcor() + horizontal_velocity)

    # Check for collision with the ground
    if ball.ycor() < -250:
        ball.penup()
        ball.sety(-250)
        velocity *= -0.8  # Bounce with some energy loss
        ball.pendown()

    if ball.xcor() > 450:
        ball.penup()
        ball.setx(-450)
        ball.pendown()

    # Update the screen
    window.update()

    # Check for the ball coming to a stop
    velocities.append(velocity)

    print(velocities)

    if len(velocities) >= 2:
        speed1 = velocities[-1]
        speed2 = velocities[-2]

        if abs(speed2 - speed1) < 0.01:
            break

    # Introduce a frame delay to control the frame rate
    time.sleep(frame_delay)

window.mainloop()
