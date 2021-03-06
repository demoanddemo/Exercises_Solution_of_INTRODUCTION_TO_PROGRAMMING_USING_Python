'''
**4.36 (Turtle: point in a circle?) Modify Listing 4.11 to let the program randomly generate
a point within the square whose center is the same as the circle center and
whose side is the diameter of the circle. Draw the circle and the point. Display a
message to indicate whether the point is inside the circle.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle
import random

# Prompt the user to enter the center coordinates and the radius of the circle
x1, y1 = eval(input("Enter the center of a circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))

# Generate a point coordinates in the square of the circle
x2 = random.random() * radius + x1 - radius / 2
y2 = random.random() * radius + y1 - radius / 2

# Draw the circle
turtle.penup()  # Pull the pen up
turtle.goto(x1, y1 - radius)
turtle.pendown()  # Pull the pen down
turtle.circle(radius)
# Draw the point

turtle.penup()  # Pull the pen up
turtle.goto(x2, y2)
turtle.pendown()  # Pull the pen down
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("red")
turtle.circle(3)
turtle.end_fill()  # Fill the shape

# Display the status
turtle.penup()  # Pull the pen up
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown()

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
if d <= radius:
    turtle.write("The point is inside the circle")
else:
    turtle.write("The point is outside the circle")

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
