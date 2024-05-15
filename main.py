import pygame
import sys
from button import Button
from screen import ScreenManager
from imageMaker import ImageMaker

class Main:
    """Main game loop"""

    def __init__(self):
        pygame.init()
        self.screen_manager = ScreenManager(3840, 2160)
        self.screen = self.screen_manager.initialize_screen()
        self.bg_color = (5, 0, 16)
        pygame.display.set_caption("Background Helper")

        self.buttonexit = Button(
            self.screen, "Exit Background Helper", self.screen.get_rect().width / 2 - 250, self.screen.get_rect().height / 2 - 25 - 100, 500, 50,
            button_color=(109, 173, 155), text_color=(255, 255, 255)
        )

        self.buttonplay = Button(
            self.screen, "Create Background", self.screen.get_rect().width / 2 - 250, self.screen.get_rect().height / 2 - 25, 500, 50,
            button_color=(109, 173, 155), text_color=(255, 255, 255)
        )

        self.image_maker = ImageMaker(self.screen_manager.width, self.screen_manager.height)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.buttonexit.is_clicked(mouse_pos):
                        pygame.quit()
                        sys.exit()
                    elif self.buttonplay.is_clicked(mouse_pos):
                        self.image_maker.open_new_window()
                        self.screen = self.screen_manager.initialize_screen()

            self.screen.fill(self.bg_color)
            self.buttonexit.draw_button()
            self.buttonplay.draw_button()
            pygame.display.flip()

if __name__ == "__main__":
    game = Main()
    game.run()
