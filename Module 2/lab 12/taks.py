import turtle

def draw_smiley_face():
    screen = turtle.Screen()
    screen.title("Smiley Face")
    smiley = turtle.Turtle()
    smiley.speed(1)
    # Draw face
    smiley.penup()
    smiley.goto(0, -100)
    smiley.pendown()
    smiley.circle(100)
    # Draw left eye
    smiley.penup()
    smiley.goto(-35, 35)
    smiley.pendown()
    smiley.circle(10)
    # Draw right eye
    smiley.penup()
    smiley.goto(35, 35)
    smiley.pendown()
    smiley.circle(10)
    # Draw mouth
    smiley.penup()
    smiley.goto(-40, -20)
    smiley.pendown()
    smiley.setheading(-60)
    smiley.circle(40, 120)
    turtle.done()
def main():
    draw_smiley_face()




main()
