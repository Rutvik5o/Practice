import turtle
import time

def write_char(char, delay=0.5):
    my_turtle.write(char, font=("Arial", 20, "normal"))
    my_turtle.penup()
    my_turtle.forward(15) #-> Adjusted for the forward distance for better seperation
    my_turtle.pendown()
    my_turtle.write("_", font=("Arial", 20, "normal"))
    my_turtle.penup()
    my_turtle.forward(5) #->Adjusted the forward distance
    time.sleep(delay)
    my_turtle.clear()

#-> Setting up the screen
screen = turtle.Screen()
screen.bgcolor("black")  #-> Confirming with background color

#-> Using through a Creating the turtle Object
my_turtle = turtle.Turtle()
my_turtle.speed(1) #-> Setting a slower speed for demostration
my_turtle.color("orange") 

my_turtle.penup()
my_turtle.goto(-150, 0)
my_turtle.pendown()

write_char("J")
write_char("a")
write_char("y")
write_char(" ")

write_char("S")
write_char("h")
write_char("r")
write_char("e")
write_char("e")
write_char(" ")

write_char("R")
write_char("a")
write_char("m")

my_turtle.clear()
time.sleep(1)  

my_turtle.goto(-50, 0)
my_turtle.color("orange")  
my_turtle.write("Jay Shree Ram", font=("Arial", 40, "bold"))

#-> Adding Underline For => "Jay Shree Ram"
my_turtle.penup()
my_turtle.goto(-50, -40)
my_turtle.pendown()
my_turtle.write("_" * 15, font=("Arial", 20, "normal"))

#-> Kept window till the window close by the user
turtle.done()
