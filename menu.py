import pygame
import game


class Menu:
    def __init__(self):
        pygame.init()

        self.running = True
        self.window = pygame.display.set_mode(600, 600)
        self.clock = pygame.time.Clock()

    def start(self):
        while self.running:
            self.clock.tick(60)

    def play(self):
        self.running = False
        game.start(self.window)

    def high_scores(self):
        pass


menu = Menu()

if __name__ == "__main__":
    menu.start()