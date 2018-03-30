import pygame


class Game:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()
        self.projectiles = []
        self.enemies = []

    def start(self, window):

        # noinspection PyAttributeOutsideInit
        self.window = window

        Enemy.spawn(10, 10)
        Enemy.spawn(55, 10)
        Enemy.spawn(100, 10)
        Enemy.spawn(145, 10)
        Enemy.spawn(190, 10)
        Enemy.spawn(235, 10)
        Enemy.spawn(280, 10)
        Enemy.spawn(325, 10)
        Enemy.spawn(370, 10)
        Enemy.spawn(415, 10)
        Enemy.spawn(460, 10)
        Enemy.spawn(505, 10)
        Enemy.spawn(550, 10)

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

            for enemy in self.enemies:
                enemy.draw()

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

        if right and self.x < (600 - self.vel - 80):
            self.x += self.vel

        elif not right and self.x > self.vel:
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

        if self.is_touching_enemy():
            self.despawn()

        if self.is_touching_wall():
            self.despawn()

        if self.north:
            self.y -= 5

        else:
            self.y += 5

        self.draw()

    def is_touching_enemy(self):
        touching = False

        for enemy in game.enemies:
            if enemy.y <= self.x <= enemy.x+40 and enemy.y <= self.y <= enemy.y + 40:
                touching = True
                enemy.despawn()
                break

        return touching

    def is_touching_wall(self):
        return self.y <= 0 or self.y >= 600

    def despawn(self):
        game.projectiles.remove(self)


class Enemy:

    @staticmethod
    def spawn(x, y):
        game.enemies.append(Enemy(x, y))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(game.window, (255, 255, 255), (self.x, self.y, 40, 40))

    def tick(self):
        self.draw()

    def despawn(self):
        game.enemies.remove(self)


game = Game()

if __name__ == "__main__":
    game.start(pygame.display.set_mode((600, 600)))
