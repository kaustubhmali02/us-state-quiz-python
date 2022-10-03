from turtle import Turtle
FONT = ("Courier", 10, "normal")


class StateNames(Turtle):
    def __init__(self, state_name, position):
        super().__init__()
        self.state_name = state_name
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("black")
        self.update_state_name()

    def update_state_name(self):
        self.write(f"{self.state_name}", False, align="center", font=FONT)
