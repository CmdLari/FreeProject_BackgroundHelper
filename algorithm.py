from imageMaker import ImageMaker
import random
import pygame
import os
import time

def algorithm(screen, setting, screenwidth, screenheight):
    part = "canvas"
    canvas(screen, setting, part, screenwidth, screenheight)
    part = "background"
    background(screen, setting, part, screenwidth, screenheight)
    part = "athmo"
    athmo(screen, setting, part, screenwidth, screenheight)
    part = "middle"
    middle(screen, setting, part, screenwidth, screenheight)
    part = "foreground"
    foreground(screen, setting, part, screenwidth, screenheight)
    part = "frame"
    frame(screen, setting, part, screenwidth, screenheight)
    
    if not os.path.exists('output'):
        os.makedirs('output')
    
    window_surface = pygame.display.get_surface()
    filename = os.path.join('output', f'screenshot_{int(time.time())}.png')
    pygame.image.save(window_surface, filename)


def canvas(screen, setting, part, screenwidth, screenheight):
    ### BACKGROUND
    random_background = random.randint(0, 3)
    ImageMaker.blit_image(screen, setting, part, random_background, screenwidth, screenheight, 0, 0, 0)

def background(screen, setting, part, screenwidth, screenheight):
    random_recursion = random.randint(0,10)
    random_background = random.randint(0, 3)
    randy = random.randint(-25,25)
    randx = random.randint((-screenwidth)/2,screenwidth/2)
    flip = random.randint(0, 1)
    ImageMaker.blit_image(screen, setting, part, random_background, screenwidth, screenheight, 0+randx, 0+randy, flip)
    if random_recursion>0:
        background(screen, setting, part, screenwidth, screenheight)
        
def athmo(screen, setting, part, screenwidth, screenheight):
    random_recursion = random.randint(0,3)
    random_background = random.randint(0, 3)
    randy = random.randint(-25,25)
    randx = random.randint((-screenwidth)/2,screenwidth/2)
    flip = random.randint(0, 1)
    ImageMaker.blit_image(screen, setting, part, random_background, screenwidth, screenheight, 0+randx, 0+randy, flip)
    if random_recursion>0:
        athmo(screen, setting, part, screenwidth, screenheight)
        
def middle(screen, setting, part, screenwidth, screenheight):
    random_recursion = random.randint(0,4)
    random_background = random.randint(0, 3)
    randy = random.randint(-25,25)
    randx = random.randint((-screenwidth)/2,screenwidth/2)
    flip = random.randint(0, 1)
    ImageMaker.blit_image(screen, setting, part, random_background, screenwidth, screenheight, 0+randx, 0+randy, flip)
    if random_recursion>0:
        middle(screen, setting, part, screenwidth, screenheight)

def foreground(screen, setting, part, screenwidth, screenheight):
    random_recursion = random.randint(0,6)
    random_background = random.randint(0, 3)
    if random_background==3:
        yesno = random.randint(0, 1)
        if yesno==1:
            random_background = random.randint(0, 3)
    randy = random.randint(-25,25)
    randx = random.randint((-100),100)
    flip = random.randint(0, 1)
    ImageMaker.blit_image(screen, setting, part, random_background, screenwidth, screenheight, 0+randx, 0+randy, flip)
    if random_recursion>0:
        foreground(screen, setting, part, screenwidth, screenheight)

def frame(screen, setting, part, screenwidth, screenheight):
    random_recursion = random.randint(0,4)
    random_background = random.randint(0, 3)
    flip = random.randint(0, 1)
    ImageMaker.blit_image(screen, setting, part, random_background, screenwidth, screenheight, 0, 0, flip)
    if random_recursion>0:
        frame(screen, setting, part, screenwidth, screenheight)