import pygame
import sys
from button import Button 

class Main:
    """Main game loop"""

    def __init__(self):
        pygame.init()
        self.screen_width = 3840
        self.screen_height = 2160
        self.bg_color = (5, 0, 16)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Background Helper")

        self.buttonexit = Button(
            self.screen, "Exit Background Helper", self.screen_width/2-250, self.screen_height/2-25-100, 500, 50,
            button_color=(109, 173, 155), text_color=(255, 255, 255)
        )

        self.buttonplay = Button(
            self.screen, "Create Background", self.screen_width/2-250, self.screen_height/2-25, 500, 50,
            button_color=(109, 173, 155), text_color=(255, 255, 255)
        )


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

            self.screen.fill(self.bg_color)
            self.buttonexit.draw_button()
            self.buttonplay.draw_button()
            pygame.display.flip()

if __name__ == "__main__":
    game = Main()
    game.run()
