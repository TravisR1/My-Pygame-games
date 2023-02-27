#follow the numbers
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0
bg = Actor("bg")

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(30, WIDTH - 30) , randint(30, HEIGHT - 30)
    dots.append(actor)

def draw():
    bg.draw()
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 20))
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
def on_mouse_down(pos):
    global next_dot, lines
    if dots[next_dot].collidepoint(pos):
        sounds.coin_collected.play
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1

    else:
        lines = []
        next_dot = 0

