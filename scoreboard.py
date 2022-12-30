from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.sety(250)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game over", move=False, align='center', font=('Arial', 24, 'normal'))
