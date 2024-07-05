'''Игра Пинг-Понг'''
from pygame import *
import random 


class Racket():
    def __init__(self, speed, x, y, color):
        self.speed = speed
        self.rect = Rect(x, y, 15, 100)
        self.color = color

    def move_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys_pressed[K_s] and self.rect.y < height - 100:
            self.rect.y += self.speed

    def move_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys_pressed[K_DOWN] and self.rect.y < height - 100:
            self.rect.y += self.speed

    def reset(self):
        draw.rect(window, self.color, self.rect)

class Ball():
    def __init__(self, ball_image, speed, x, y):
        self.image = transform.scale(image.load(ball_image), (70, 70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def start_move(self):
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])


height = 700
width = 1000
window = display.set_mode((width, height))
window.fill((127, 208, 255))
display.set_caption('Пинг-Понг')
clock = time.Clock()
fps = 60
finish = False
racket1 = Racket(speed=10, x=10 , y=350, color=(255, 4, 4))
racket2 = Racket(speed=10, x=980 , y=350, color=(255, 244, 58))
ball = Ball('ball.jpg', speed=10, x=500, y=350)
font.init()
font1 = font.Font(None, 40)
win1 = font1.render('Player 1 WON', True, (255, 244, 56))
win2 = font1.render('Player 2 WON', True, (255, 244, 56))
i = 0
ball.start_move()

game = True
while game:
    window.fill((127, 208, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:      
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
        racket1.reset()
        racket2.reset()
        ball.reset()

    if ball.rect.y >= height - 70 or ball.rect.y <= 0:
        ball.speed_y *= -1

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        ball.speed_x *= -1
        i += 1
        if i % 4 == 0:
            ball.speed_x *= 1.5
            ball.speed_y *= 1.5

    if ball.rect.x <= 0:
        finish = True
        window.blit(win2, (width/2, height/2))
    elif ball.rect.x >= width:
        finish = True
        window.blit(win1, (width/2-200, height/2))
    
    racket1.move_left()
    racket2.move_right()
    
    clock.tick(fps)
    display.update()