import pygame


class Game:

    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()
        self.projectiles = []

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

            for projectile in self.projectiles:
                projectile.tick()

            pygame.display.flip()
            pygame.display.update()

    def check_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.move(False)

        elif keys[pygame.K_RIGHT]:
            self.player.move(True)

        if keys[pygame.K_SPACE]:
            self.player.fire_projectile()


class Player:

    def __init__(self):
        self.x = 250
        self.y = 540
        self.vel = 6

        self.fire_cooldown = 0

        self.image = pygame.image.load("player.png")

    @property
    def location(self):
        return self.x, self.y

    def draw(self):
        game.window.blit(self.image, self.location)
        self.fire_cooldown -= 1

    def fire_projectile(self):
        if self.fire_cooldown < 0:
            self.fire_cooldown = 5
            Projectile(True, self).fire()

    def move(self, right):
        if right:
            self.x += self.vel

        else:
            self.x -= self.vel


class Projectile:

    def __init__(self, north, entity):
        self.north = north
        self.entity = entity

        if self.north:
            self.x = entity.x+38
            self.y = entity.y+10

    def fire(self):
        game.projectiles.append(self)

    def draw(self):
        pygame.draw.rect(game.window, (255, 255, 255), (self.x, self.y, 3, 8))

    def tick(self):
        if self.north:
            self.y -= 5

        else:
            self.y += 5

        self.draw()


game = Game()

if __name__ == "__main__":
    game.start()
