import tkinter as tk
from random import randrange as rnd, choice


class Ball:
    def __init__(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.step_x, self.step_y = +10, +10
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.my_ball = canvas.create_oval(self.x - self.r, self.y - self.r,
                                          self.x + self.r, self.y + self.r,
                                          fill=choice(colors), width=0)

    def move(self):
        self.x += self.step_x
        self.y += self.step_y
        if self.x + self.r > canvas.winfo_width() or self.x - self.r <= 0:
            self.step_x = -self.step_x
            self.step_y = rnd(-10, 10)
        if self.y + self.r > canvas.winfo_height() or self.y - self.r <= 0:
            self.step_y = -self.step_y
            self.step_x = rnd(-10, 10)

    def show(self):
        canvas.move(self.my_ball, self.step_x, self.step_y)


def ball_move(ball_ids):
    for ball_id in ball_ids:
        ball_id.move()
        ball_id.show()
    root.after(50, ball_move, ball_ids)


def click(event):
    print('click')


def main():
    global canvas, root
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    b = [Ball() for i in range(5)]
    ball_move(b)
    canvas.bind('<Button-1>', click)
    tk.mainloop()


if __name__ == '__main__':
    main()
