import turtle

my_var = turtle.Turtle()

my_var.getscreen().bgcolor("#51D247")     #colorspire.com/

my_var.speed(10)
my_var.penup()
my_var.goto((0, -50))
my_var.pendown()


def circle(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            my_var.circle(size)
            circle(turtle, size / 1.3)


circle(my_var, 180)

turtle.done()