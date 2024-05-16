import pygame
from screen import ScreenManager
from button import Button
from algorithm import algorithm

class Main:
    """Main game loop"""

    def __init__(self):
        pygame.init()
        self.show_return_button = False  # Initialize button visibility flag

    def open_new_screen(self, screen_manager, backgroundsetting):
        new_screen = pygame.Surface((screen_manager.width, screen_manager.height))
        new_screen.fill((0, 0, 0))
        return_button = Button(screen_manager.screen, "X", 0, 0, 20, 20, (110, 150, 120), (255, 255, 255))
        screen_manager.screen.blit(new_screen, (0, 0))
        algorithm(screen_manager.screen, backgroundsetting, screen_manager.width, screen_manager.height)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if return_button.is_clicked(mouse_pos):
                        self.show_return_button = False  # Hide the button when clicked
                        running = False

            if self.show_return_button:
                return_button.draw_button()

            pygame.display.update()

    def draw_text(self, screen, text, pos, font_size=20, color=(255, 255, 255)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, pos)

    def run(self):
        backgroundsetting = "forest"

        screen_manager = ScreenManager(1920, 1080)  # Set your desired width and height
        pygame.display.set_caption("Your Game Title")
        screen_manager.screen = pygame.display.set_mode((screen_manager.width, screen_manager.height), pygame.FULLSCREEN)

        quit_button = Button(screen_manager.screen, "QUIT", screen_manager.width / 2 - 50, screen_manager.height / 2 - 75, 100, 50, (110, 150, 120), (255, 255, 255))
        background_button = Button(screen_manager.screen, "CREATE", screen_manager.width / 2 - 50, screen_manager.height / 2, 100, 50, (110, 150, 120), (255, 255, 255))
        forest_button = Button(screen_manager.screen, "FOREST", screen_manager.width / 2 - 50, screen_manager.height / 2 + 75, 100, 50, (110, 150, 120), (255, 255, 255))

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
                    if quit_button.is_clicked(mouse_pos):
                        running = False
                    elif background_button.is_clicked(mouse_pos):
                        self.show_return_button = True
                        self.open_new_screen(screen_manager, backgroundsetting)
                    elif forest_button.is_clicked(mouse_pos):
                        backgroundsetting = "forest"

            screen_manager.screen.fill((0, 0, 0))  # Clear screen
            quit_button.draw_button()
            background_button.draw_button()
            forest_button.draw_button()

            # Draw license text
            self.draw_text(screen_manager.screen, "Assets are under artistic license.", (100, screen_manager.height - 60), font_size=20, color=(255, 255, 255))
            self.draw_text(screen_manager.screen, "Please do not publish results using these assets and replace them with your own for any non-private usage.", (100, screen_manager.height - 40), font_size=20, color=(255, 255, 255))

            pygame.display.update()

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Main()
    game.run()
