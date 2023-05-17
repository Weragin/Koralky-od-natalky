import tkinter as tk
from random import randint

corals = []
done = []
WIDTH = 800
HEIGHT = 400
CORAL_WIDTH = 20
CORAL_HEIGHT = 20
corals_colours = [0, 1, 2, 3] * 10
CORALS_COUNT = 40
RIVET_COORDS = []

root = tk.Tk()
root.geometry(f'{WIDTH + 10}x{HEIGHT + 10}')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, background='white')
canvas.pack()


def setup():
    global corals, WIDTH, HEIGHT, CORAL_WIDTH, CORAL_HEIGHT, corals_colours, CORALS_COUNT
    for i in range(CORALS_COUNT):
        x = randint(1, WIDTH - CORAL_WIDTH)
        y = randint(1, HEIGHT - CORAL_HEIGHT*2)
        index = randint(0, len(corals_colours)-1)
        colour = corals_colours.pop(index)
        # coral = tk.PhotoImage(f'data/Python_Cup_2020/assets/koralik{colour}')
        corals.append(canvas.create_oval(x, y, x + CORAL_WIDTH, y + CORAL_HEIGHT))


def click(e):
    global corals, done
    canvas.unbind('<1>')
    overlaps = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    print(overlaps)
    if len(overlaps) > 0:
        if overlaps[-1] in corals:
            movement1(overlaps)


def movement1(coral):
    global RIVET_COORDS
    coral_pos = canvas.coords(coral)
    dx = RIVET_COORDS[2] - coral_pos[0]
    dy = (RIVET_COORDS[3] - RIVET_COORDS[1])//2 - (coral_pos[3] - coral_pos[1])//2
    if dx > 0 and dy > 0:
        if dx > dy:
            dx //= dy
            dy = 1
        else:
            dy //= dx
            dx = 1
        canvas.move(coral, dx, dy)
        canvas.after(2, movement1(coral))
    movement2(coral)


def movement2(coral):
    pass


rivet = tk.PhotoImage(file='data/assets/Python_Cup_2020/koralik_nit.png')
print(rivet.width(), rivet.height())
# canvas.create_image(WIDTH - rivet.width(), HEIGHT - rivet.height(), anchor='nw', image=rivet)
canvas.create_image(0, 0, anchor='nw', image=rivet)

canvas.bind('<1>', click)


setup()
root.mainloop()
