import pygame

class ScreenManager:
    """Class to handle screen initialization and management"""

    def __init__(self, width, height, fullscreen=True):
        self.width = width
        self.height = height
        self.screen = None
