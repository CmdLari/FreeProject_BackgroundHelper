import pygame

class Button:
    """Class to create a button"""

    def __init__(self, screen, msg, x, y, width, height, button_color, text_color):
        self.screen = screen
        self.msg = msg
        self.rect = pygame.Rect(x, y, width, height)
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 20)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def is_clicked(self, mouse_pos):
        """Check if the button is clicked"""
        return self.rect.collidepoint(mouse_pos)