# Imports.
import pygame
import game
 
 
# Class to represent the menu.
class Menu:

    # Function to initialise the menu.
    def __init__(self):

        # Initialise pygame.
        pygame.init()
 
        # Create window, and variables to control game loop.
        self.running = True
        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        # Load the font.
        self.font = pygame.font.Font("LCD_Solid.ttf", 80)

        # Render required text using the font.
        self.play_text = self.font.render("PLAY", True, (0, 0, 0))
        self.high_scores_text = self.font.render("TOP", True, (0, 0, 0))
 
    # Function to open the window.
    def start(self):

        # Main game loop.
        while self.running:

            # Tick the clock at 60fps and fill the window black.
            self.clock.tick(60)
            self.window.fill((0, 0, 0))

            # Get the mouse pointer location and whether the left click was pressed.
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()[0]

            # Check if the mouse is over the play button.
            if 200 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 400:

                # Fill the play button in white.
                pygame.draw.rect(self.window, (255, 255, 255), (200, 300, 200, 100))

                # Play the game if the play button is clicked.
                if mouse_pressed:
                    self.play()

            else:
                # Fill the play button gray.
                pygame.draw.rect(self.window, (200, 200, 200), (200, 300, 200, 100))

            # Check if the mouse is over the high scores button.
            if 200 <= mouse_pos[0] <= 400 and 450 <= mouse_pos[1] <= 550:

                # Fill the high score button white.
                pygame.draw.rect(self.window, (255, 255, 255), (200, 450, 200, 550))

                # Show high scores if the button is pressed.
                if mouse_pressed:
                    self.high_scores()

            else:
                # Fill the button gray.
                pygame.draw.rect(self.window, (200, 200, 200), (200, 450, 200, 550))

            # Put text on top of buttons.
            self.window.blit(self.play_text, (210, 310))
            self.window.blit(self.high_scores_text, (210, 460))

            # Check if game has been exited, stop loop if so.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Swap buffers and update the display.
            pygame.display.flip()
            pygame.display.update()
 
    # Method to start the game.
    def play(self):

        # Stop the menu running and start the game.
        self.running = False
        game.game.start(self.window)
 
    # Method to show high scores.
    def high_scores(self):
        pass
 
 
# Create a new menu.
menu = Menu()
 
# If this module has been run directly, start the game.
if __name__ == "__main__":
    menu.start()
