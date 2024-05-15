import pygame
from screen import ScreenManager
from button import Button
from imageMaker import ImageMaker
# from algorithm import Algorithm

class Main:
    """Main game loop"""

    def __init__(self):
        pygame.init()

    def run(self):
        backgroundsetting = "forest"

        screen_manager = ScreenManager(1920, 1080)  # Set your desired width and height
        pygame.display.set_caption("Your Game Title")
        screen_manager.screen = pygame.display.set_mode((screen_manager.width, screen_manager.height), pygame.FULLSCREEN)

        quit_button = Button(screen_manager.screen, "QUIT", screen_manager.width/2-50, screen_manager.height/2-75, 100, 50, (110, 150, 120), (255, 255, 255))
        background_button = Button(screen_manager.screen, "CREATE", screen_manager.width/2-50, screen_manager.height/2, 100, 50, (110, 150, 120), (255, 255, 255))
        forest_button = Button(screen_manager.screen, "FOREST", screen_manager.width/2-50, screen_manager.height/2+75, 100, 50, (110, 150, 120), (255, 255, 255))

        def open_new_screen():
            show_button = True
            new_screen = pygame.Surface((screen_manager.width, screen_manager.height))
            new_screen.fill((255, 255, 255))  # Fill the new screen with white
            return_button = Button(screen_manager.screen, "X", 0, 0, 20, 20, (110, 150, 120), (255, 255, 255))

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if return_button.is_clicked(mouse_pos):
                            running = False
                            show_button = False

                # Blit the image onto the new screen, fitting the screen size

                screen_manager.screen.blit(new_screen, (0, 0))  # Blit the new screen onto the main screen
                if show_button:
                    ImageMaker.blit_image(screen_manager.screen, backgroundsetting, "canvas", 0, screen_manager.width, screen_manager.height)
                    return_button.draw_button()
                pygame.display.update()


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
                        open_new_screen()
                    elif forest_button.is_clicked(mouse_pos):
                        backgroundsetting = "forest"

            quit_button.draw_button()
            background_button.draw_button()
            forest_button.draw_button()

            pygame.display.update()

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Main()
    game.run()
