# import
import pygame
import random
pygame.init()

# Screen size
width = 700
length = 700

# background
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (width,length))

#Sound
sound = pygame.mixer.Sound("perfect-beauty-191271.mp3")

# Colours
Red = (255,0,0)
White = (255,255,255)

# Screen
screen =  pygame.display.set_mode((width,length))
pygame.display.set_caption("Bouncing ball")

# BAll porperties
def create_balls():
    speed = [random.randint(1,10),random.randint(1,10)]
    radius = random.randint(10,40)
    colour = [random.randint(0,255),random.randint(0,255),random.randint(00,255)]
    position = [random.randint(radius,width-radius),random.randint(radius,length-radius)]
    return {'Radius':radius,'Colour':colour,'Speed':speed,'Position':position}

# No of balls
multiple_balls = [create_balls() for i in range(20)]

#Clock
Clock = pygame.time.Clock()

# Game quiting
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Boder collitions
    for ball in multiple_balls:
        ball['Position'][0] += ball['Speed'][0]
        ball['Position'][1] += ball['Speed'][1]

        if ball['Position'][0] <= 0 or ball['Position'][0] >= width:
            ball['Speed'][0] = - ball['Speed'][0]
            sound.play()
        if ball['Position'][1] <= 0 or ball['Position'][1] >= length:
            ball['Speed'][1] = - ball['Speed'][1]
            sound.play()

    screen.blit(bg,(0,0))
    for ball in multiple_balls:
        pygame.draw.circle(screen,ball['Colour'],(ball['Position'][0],ball['Position'][1]),ball['Radius'])

    pygame.display.update()

    Clock.tick(60)

