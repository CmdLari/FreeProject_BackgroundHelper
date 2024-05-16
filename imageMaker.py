import os
import pygame

class ImageMaker:
    """Class to handle image manipulation"""

    @staticmethod
    def blit_image(screen, backgroundsetting, part, number, screen_width, screen_height, x, y, flip):
        image_path = os.path.join("assets", f"{backgroundsetting}{part}{number}.png")
        image = pygame.image.load(image_path)
        
        image = pygame.transform.scale(image, (screen_width, screen_height))
        if flip == 1:
            image = pygame.transform.flip(image, True, False)
        
        # Blit the image to the screen
        screen.blit(image, (x, y))
