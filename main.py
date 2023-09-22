import turtle as t
import random
tim = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b


tim.speed(0)
tim.width(1)
def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


# direction = [0, 90, 180, 270]
#
# for i in range (1000):
#     tim.forward(50)
#     tim.setheading(random.choice(direction))
#     tim.color(random_colour())
