from turtle import Turtle

FONTS = ('Ariel', 18, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONTS)

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONTS)


