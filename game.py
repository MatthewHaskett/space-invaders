import pygame

class Game():
    
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((400, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()

    def start(self):

        pygame.display.set_caption("Space Invaders")
        
        while self.running:
            self.clock.tick(60)

            self.check_movement()

            self.window.fill((0, 0, 0))
            self.player.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            pygame.display.update()


    def check_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x -= self.player.vel

        elif keys[pygame.K_RIGHT]:
            self.player.x += self.player.vel
        

class Player():

    def __init__(self):
        self.x = 200
        self.y = 500
        self.vel = 6

        self.image = pygame.image.load("player.png")

    @property
    def location(self):
        return self.x, self.y

    def draw(self):
        game.window.blit(self.image, self.location)
    
game = Game()

if __name__ == "__main__":
    game.start()
