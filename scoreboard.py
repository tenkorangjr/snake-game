from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", mode='r') as highscore_file:
            self.highscore = int(highscore_file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((0, 270))
        self.show_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_scoreboard()

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def show_scoreboard(self):
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_board(self):
        self.clear()
        self.score = 0
        self.goto(0, 270)
        self.show_scoreboard()

    def update_highscore(self):
        if self.score > self.highscore:
            with open(file="highscore.txt", mode='w') as highscore_file:
                self.highscore = self.score
                highscore_file.write(str(self.highscore))

