from imageMaker import ImageMaker
from screen import ScreenManager
import random

def algorithm(screen, setting, screenwidth, screenheight):
    random_recursion = random.randint(0,1)
    part = "canvas"
    background(screen, setting, part, screenwidth, screenheight)



def background(screen, setting, part, screenwidth, screenheight):
    ### BACKGROUND
    random_background = random.randint(0, 3)
    ImageMaker.blit_image(screen, setting, part, random_background, screenwidth, screenheight, 0, 0)
