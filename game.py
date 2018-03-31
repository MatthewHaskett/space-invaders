import pygame


class Game:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()
        self.projectiles = []
        self.enemies = {}
        self.enemies_by_line = {}

        self.lowest_line = 0

    def start(self, window):

        # noinspection PyAttributeOutsideInit
        self.window = window

        Enemy.spawn_new_line()
        Enemy.spawn_new_line()
        Enemy.spawn_new_line()

        print(self.enemies)

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

            for location in self.enemies:
                self.enemies[location].draw()

            pygame.display.flip()
            pygame.display.update()

    def check_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.move(False)

        if keys[pygame.K_RIGHT]:
            self.player.move(True)

        if keys[pygame.K_SPACE]:
            self.player.fire_projectile()

    def move_down(self, row):
        self.enemies_by_line[row-1] = self.enemies_by_line[row]

        for enemy in self.enemies_by_line[row-1]:
            enemy.y += 50

            del self.enemies[(enemy.x, enemy.y-50)]
            self.enemies[(enemy.x, enemy.y)] = enemy


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

        for location in game.enemies:
            enemy = game.enemies[location]

            if enemy.x <= self.x <= enemy.x+40 and enemy.y <= self.y <= enemy.y + 40:
                touching = True
                del game.enemies[location]
                break

        return touching

    def is_touching_wall(self):
        return self.y <= 0 or self.y >= 600

    def despawn(self):
        game.projectiles.remove(self)


class Enemy:

    @staticmethod
    def spawn_new_line():
        if 2 in game.enemies_by_line.keys():
            game.move_down(2)

        if 3 in game.enemies_by_line.keys():
            game.move_down(3)

        if 4 in game.enemies_by_line.keys():
            game.move_down(4)

        if 5 in game.enemies_by_line.keys():
            game.move_down(5)

        game.enemies_by_line[5] = []

        Enemy.spawn(10, 50)
        Enemy.spawn(55, 50)
        Enemy.spawn(100, 50)
        Enemy.spawn(145, 50)
        Enemy.spawn(190, 50)
        Enemy.spawn(235, 50)
        Enemy.spawn(280, 50)
        Enemy.spawn(325, 50)
        Enemy.spawn(370, 50)
        Enemy.spawn(415, 50)
        Enemy.spawn(460, 50)
        Enemy.spawn(505, 50)
        Enemy.spawn(550, 50)

    @staticmethod
    def spawn(x, y):
        enemy = Enemy(x, y)

        game.enemies[(x, y)] = enemy
        game.enemies_by_line[5].append(enemy)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("enemy.png")

    def __str__(self):
        return "Enemy at: {}".format(self.location)

    def __repr__(self):
        return "Enemy.spawn({})".format(self.location)

    @property
    def location(self):
        return self.x, self.y

    def draw(self):
        game.window.blit(self.image, self.location)

    def tick(self):
        self.draw()


game = Game()

if __name__ == "__main__":
    game.start(pygame.display.set_mode((600, 600)))
