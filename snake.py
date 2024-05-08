from turtle import Turtle


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        # print(self.turtles)

    def create_snake(self):
        x = 0
        y = 0
        for n in range(3):
            leonardo = Turtle("circle")
            leonardo.color("cadet blue")
            leonardo.penup()
            leonardo.setpos(x, y)
            leonardo.speed("fastest")
            self.turtles.append(leonardo)
            x -= 20

    def extend(self):
        leonardo = Turtle("circle")
        leonardo.color("cadet blue")
        leonardo.penup()
        leonardo.speed("fastest")
        x = self.turtles[-1].xcor()
        y = self.turtles[-1].ycor()
        leonardo.goto(x, y)
        self.turtles.append(leonardo)

    def move(self):
        for n in range(len(self.turtles)-1, 0, -1):
            x = self.turtles[n-1].xcor()
            y = self.turtles[n-1].ycor()
            self.turtles[n].setposition(x, y)
        self.head.forward(20)

    def reset_snake(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)

        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def up(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)
