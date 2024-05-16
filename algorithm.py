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

    if not os.path.exists('output'):
        os.makedirs('output')
    
    window_surface = pygame.display.get_surface()
    filename = os.path.join('output', f'screenshot_{int(time.time())}.jpeg')
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
