from turtle import Turtle, Screen

Tom = Turtle()
screen = Screen()

def move_forward():
    Tom.forward(10)
    
def move_backward():
    Tom.backward(10)
    
def turn_left():
    new_heading = Tom.heading() + 10
    Tom.setheading(new_heading)
    
def turn_right():
    new_heading = Tom.heading() - 10
    Tom.setheading(new_heading)

def undo_thing():
    Tom.undo()
    
def clear_screen():
    Tom.clear()
    Tom.penup()
    Tom.home()
    Tom.pendown()
    
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")
screen.onkey(undo_thing, "z")

screen.exitonclick()
