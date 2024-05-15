import pygame

class ScreenManager:
    """Class to handle screen initialization and management"""

    def __init__(self, width, height, fullscreen=True):
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.screen = None

    def initialize_screen(self):
        """Initialize the screen based on the current settings"""
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.width = self.screen.get_rect().width
            self.height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        return self.screen

    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        self.fullscreen = not self.fullscreen
        self.initialize_screen()

    def get_screen(self):
        """Get the current screen surface"""
        return self.screen
