import pygame
import sys
from screen import ScreenManager
from button import Button

class ImageMaker:
    """Class to handle creating a new window"""

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_manager = ScreenManager(screen_width, screen_height, fullscreen=False)

    def open_new_window(self):
        pygame.display.quit()  # Quit the current display
        pygame.display.init()  # Re-initialize the display

        new_screen = self.screen_manager.initialize_screen()
        pygame.display.set_caption("New Window")

        button_back = Button(
            new_screen, "Back to Main Window", self.screen_width / 2 - 250, self.screen_height / 2 - 25, 500, 50,
            button_color=(109, 173, 155), text_color=(255, 255, 255)
        )

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_back.is_clicked(mouse_pos):
                        self.return_to_main_window()
                        return

            new_screen.fill((0, 0, 0))  # Fill the new window with black color
            button_back.draw_button()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def return_to_main_window(self):
        pygame.display.quit()
        pygame.display.init()
        screen_manager = ScreenManager(self.screen_width, self.screen_height, fullscreen=True)
        screen_manager.initialize_screen()
