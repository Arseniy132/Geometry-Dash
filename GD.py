from pygame import *
import os

init()
mixer.init()

clock = time.Clock()
screen = display.set_mode((1000, 800))
display.set_caption("Geometry Dash")
display.set_icon(image.load("icon.png"))
a = 650
while True:
    display.update()
    clock.tick(60)

    player = draw.rect(screen, (255, 0, 0), (75, a, 50, 50), width=6)

    for e in event.get():
        if e.type == QUIT:
            quit()
        elif e.type == KEYDOWN and e.key == K_SPACE:
            a -= 40
