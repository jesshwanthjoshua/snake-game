from turtle import Turtle



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.setposition(0, 380)
        self.write(f"Score Board: {self.score}      High Score = {self.high_score}", False, 'center', ('sans serif', 10, 'italic'))

    def score_count(self):
        self.clear()
        self.write(f"Score Board: {self.score}      High Score = {self.high_score}", False, 'center', ('sans serif', 10, 'italic'))

    def high_score_count(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.score_count()
