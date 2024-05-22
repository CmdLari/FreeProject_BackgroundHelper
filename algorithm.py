from imageMaker import ImageMaker
import random
import pygame
import os
import time

def algorithm(screen, setting, screenwidth, screenheight):
    part = "canvas"
    choseImg(screen, setting, part, screenwidth, screenheight, 0, 0, 0, 0, 0)
    part = "background"
    choseImg(screen, setting, part, screenwidth, screenheight, 0, 0, -25, 25, 10)
    part = "athmo"
    choseImg(screen, setting, part, screenwidth, screenheight, -screenwidth/2, screenwidth/2, -25, 25, 3)
    part = "middle"
    choseImg(screen, setting, part, screenwidth, screenheight, -screenwidth/2, screenwidth/2, -25, 25, 4)
    part = "foreground"
    choseImg(screen, setting, part, screenwidth, screenheight, -100, 100, -25, 25, 6)
    part = "frame"
    choseImg(screen, setting, part, screenwidth, screenheight, 0, 0, 0, 0, 4)

    if not os.path.exists('output'):
        os.makedirs('output')
    
    window_surface = pygame.display.get_surface()
    filename = os.path.join('output', f'screenshot_{int(time.time())}.png')
    pygame.image.save(window_surface, filename)


def choseImg(screen, setting, part, screenwidth, screenheight, randXValmin, randXValmax, randYValmin, randYValmax, recursion):
    random_recursion = random.randint(0, recursion)
    random_img = random.randint(0, 3)
    randx = random.randint(randXValmin, randXValmax)
    randy = random.randint(randYValmin, randYValmax)
    flip = random.randint(0, 1)
    ImageMaker.blit_image(screen, setting, part, random_img, screenwidth, screenheight, 0+randx, 0+randy, flip)
    if random_recursion>0:
        choseImg(screen, setting, part, screenwidth, screenheight, randXValmin, randXValmax, randYValmin, randYValmax, recursion)