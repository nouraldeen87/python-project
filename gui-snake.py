import turtle
import time
import random
import tkinter as tk
from tkinter import messagebox

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.delay = 0.1
        self.score = 0
        self.high_score = 0

        self.wn = turtle.Screen()
        self.wn.title("Snake Game by nour eddin & ahmad")
        self.wn.bgcolor("black")

        self.wn.setup(width=600, height=600)

        self.wn.cv._rootwindow.resizable(False, False)
        self.wn.tracer(0)

        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("yellow")
        self.head.penup()
        self.head.speed(0)
        self.head.goto(0, 0)
        self.head.direction = "Stop"

        self.food = turtle.Turtle()
        self.colors = random.choice(["red"])
        self.shapes = random.choice(["circle"])
        self.food.shape(self.shapes)
        self.food.color(self.colors)
        self.food.penup()
        self.food.speed(0)
        self.food.goto(0, 100)

        self.pen = turtle.Turtle()
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.speed(0)
        self.pen.goto(0, 250)
        self.pen.hideturtle()
        self.pen.write("Score: 0   High Score: 0", align="center", font=("Arial", 24, "bold"))

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.destroy()

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def start_game(self):
        self.wn.listen()
        self.wn.onkeypress(self.go_up, "w")
        self.wn.onkeypress(self.go_down, "s")
        self.wn.onkeypress(self.go_left, "a")
        self.wn.onkeypress(self.go_right, "d")

        self.segments = []

        while True:
            self.wn.update()

            if (
                self.head.xcor() > 290
                or self.head.xcor() < -290
                or self.head.ycor() > 290
                or self.head.ycor() < -290
            ):
                self.game_over()

            if self.head.distance(self.food) < 20:
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                self.food.goto(x, y)

                new_segment = turtle.Turtle()
                new_segment.shape("square")
                new_segment.color("yellow")
                new_segment.speed(0)
                new_segment.penup()
                self.segments.append(new_segment)
                self.delay -= 0.001
                self.score += 10

                if self.score > self.high_score:
                    self.high_score = self.score
                    self.update_score()

            for index in range(len(self.segments) - 1, 0, -1):
                x = self.segments[index - 1].xcor()
                y = self.segments[index - 1].ycor()
                self.segments[index].goto(x, y)

            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            self.move()
            time.sleep(self.delay)

    def game_over(self):
        messagebox.showinfo("Game Over", "Your score: {}".format(self.score))
        self.reset_game()

    def reset_game(self):
        self.head.goto(0, 0)
        self.head.direction = "Stop"
        self.colors = random.choice(["red"])
        self.shapes = random.choice(["circle"])
        self.food.shape(self.shapes)
        self.food.color(self.colors)
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.score = 0
        self.delay = 0.1
        self.update_score()

    def update_score(self):
        self.pen.clear()
        self.pen.write(
            "Score: {}   High Score: {}".format(self.score, self.high_score),
            align="center",
            font=("Arial", 24, "bold"),
        )

class SnakeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.snake_game = SnakeGame(self.root)

    def run(self):
        self.root.mainloop()

snake_app = SnakeApp()
snake_app.snake_game.start_game()
snake_app.run()