import pygame
import game
 
 
class Menu:
    def __init__(self):
        pygame.init()
 
        self.running = True
        self.window = pygame.display.set_mode(600, 600)
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("LCD_Solid.tff", 80)

        self.play_text = self.font.render("PLAY")
        self.high_scores_text = self.font.render("TOP")
 
    def start(self):
        while self.running:
            self.clock.tick(60)
            self.window.fill((0, 0, 0))

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()[0]

            if 200 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 400
                pygame.draw.rect(self.window, (255, 255, 255), (200, 300, 200, 100))

                if mouse_pressed:
                    self.play()

            else:
                pygame.draw.rect(self.window, (200, 200, 200), (200, 300, 200, 100))

            if 200 <= mouse_pos[0] <= 400 and 450 <= mouse_pos[1] <= 550
                pygame.draw.rect(self.window, (255, 255, 255), (200, 450, 200, 550))

                if mouse_pressed:
                    self.high_scores()

            else:
                pygame.draw.rect(self.window, (200, 200, 200), (200, 450, 200, 550))

            self.window.blit(self.play_text, (210, 310))
            self.window.blit(self.high_scores_text, (210, 460)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            pygame.display.update()
 
    def play(self):
        self.running = False
        game.start(self.window)
 
    def high_scores(self):
        pass
 
 
menu = Menu()
 
if __name__ == "__main__":
    menu.start()