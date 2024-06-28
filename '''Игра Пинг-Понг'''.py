'''Игра Пинг-Понг'''
from pygame import *


window = display.set_mode((1000, 700))
display.set_caption('Пинг-Понг')
window.fill((36, 244, 238))
clock = time.Clock()
fps = 60

racket1 = 

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    clock.tick(fps)
    display.update()