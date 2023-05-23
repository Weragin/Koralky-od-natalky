import tkinter as tk
from random import randint, choice

corals = []
done = []
WIDTH = 780
HEIGHT = 400
CORALS_COUNT = 40


def click(e):
    global corals, done
    overlaps = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    if len(overlaps) > 0:
        if overlaps[-1] in corals:
            canvas.unbind('<1>')
            movement1(overlaps[-1])


def movement1(coral):
    coral_pos = canvas.coords(coral)
    dx = WIDTH - 90 - coral_pos[0]
    dy = HEIGHT - 41 - coral_pos[1]
    if dx != 0 and dy != 0:
        if abs(dx) > abs(dy):
            dx //= abs(dy)
            dy = 1
        else:
            dy //= abs(dx)
            dx = dx/abs(dx)
        canvas.move(coral, dx, dy)
        canvas.after(2, lambda: movement1(coral))
    else:
        movement2(coral)


def movement2(coral):
    canvas.move(coral, -1, 0)
    if canvas.coords(coral)[0] >= 60 + len(done) * corals_colours[0].width():
        canvas.after(1, lambda: movement2(coral))
    else:
        done.append(coral)
        corals.remove(coral)
        if len(done) < 10:
            canvas.bind("<1>", click)


root = tk.Tk()
root.geometry(f'{WIDTH + 10}x{HEIGHT + 10}')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, background='white')
canvas.pack()

corals_colours = [
    tk.PhotoImage(file='data/koralik0.png'),
    tk.PhotoImage(file='data/koralik1.png'),
    tk.PhotoImage(file='data/koralik2.png'),
    tk.PhotoImage(file='data/koralik3.png')
]
colour_choice = [0, 1, 2, 3] * 10

rivet_image = tk.PhotoImage(file='data/koralik_nit.png')
rivet = canvas.create_image(0, HEIGHT - 55, anchor='nw', image=rivet_image)


for i in range(CORALS_COUNT):
    x = randint(1, WIDTH - corals_colours[0].width())
    y = randint(1, HEIGHT - corals_colours[0].height() - 70)
    index = randint(0, len(colour_choice) - 1)
    colour = corals_colours[colour_choice.pop(index)]
    corals.append(canvas.create_image(x + 20, y + 20, image=colour))

canvas.bind('<1>', click)

root.mainloop()
