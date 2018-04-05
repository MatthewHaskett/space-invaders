# Imports
import pygame
import random


# Class to represent the game.
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
        self.extra_rows = 0
        self.round = 0
        self.enemy_fire_cooldown = 100
        self.row_move_cooldown = 1000

    def start(self, window):
        # noinspection PyAttributeOutsideInit
        self.window = window

        self.next_round()

        print(self.enemies)

        pygame.display.set_caption("Space Invaders")

        while self.running:
            self.clock.tick(60)

            self.check_movement()

            self.window.fill((0, 0, 0))
            self.player.draw()

            self.enemy_fire_cooldown -= 1
            self.row_move_cooldown -= 1

            if self.enemy_fire_cooldown == 0:
                self.enemy_fire_cooldown = 100

                rand = random.randint(len(self.enemies_by_line[self.lowest_line]))
                Projectile(False, self.enemies_by_line[self.lowest_line][rand]).fire()

            if self.row_move_cooldown == 0:
                self.row_move_cooldown = 1000

                if self.extra_lines > 0
                    Enemy.spawn_new_line()
                    self.extra_lines -= 1

                else:
                    if 1 in self.enemies_by_line.keys():
                        self.lose()

                    if 2 in self.enemies_by_line.keys():
                        self.move_down(2)

                    if 3 in self.enemies_by_line.keys():
                        self.move_down(3)

                    if 4 in self.enemies_by_line.keys():
                        self.move_down(4)

                    if 5 in self.enemies_by_line.keys():
                        self.move_down(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

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

        self.lowest_line = row-1

        for enemy in self.enemies_by_line[row-1]:
            enemy.y += 50

            del self.enemies[(enemy.x, enemy.y-50)]
            self.enemies[(enemy.x, enemy.y)] = enemy

    def get_rows_for_round(self):
        return (self.round // 3) + 1

    def next_round(self):
        self.round += 1
        
        start_rows = self.get_rows_for_round()

        if start_rows > 5:
            self.extra_rows = (5 - start_rows) * (-1)
            start_rows = 5

        for x in range(self.start_rows):
            Enemy.spawn_new_line()

    def lose(self):
        pass

# Class to represent the player.
class Player:
    def __init__(self):
        self.x = 250
        self.y = 540
        self.vel = 6

        self.fire_cooldown = 0
        self.score = 0
        self.lives = 3

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


# Class to represent a projectile
class Projectile:

    def __init__(self, north, entity):
        self.north = north
        self.entity = entity

        if north:
            self.x = entity.x+38
            self.y = entity.y+10

        else:
            self.x = entity.x
            self.y = entity.y

    def fire(self):
        game.projectiles.append(self)

    def draw(self):
        pygame.draw.rect(game.window, (255, 255, 255), (self.x, self.y, 3, 8))

    def tick(self):
        if self.is_touching_enemy() or self.is_touching_wall() or self.is_touching_player():
            self.despawn()

        if self.north:
            self.y -= 5

        else:
            self.y += 5

        self.draw()

    def is_touching_enemy(self):
        touching = False

        if not self.north:
            return touching

        for location in game.enemies:
            enemy = game.enemies[location]

            if enemy.x <= self.x <= enemy.x+40 and enemy.y <= self.y <= enemy.y + 40:
                touching = True
                game.enemies[location].despawn()
                break

        return touching

    def is_touching_wall(self):
        return self.y <= 0 or self.y >= 600

    def is_touching_player(self):
        touching = False

        if self.north:
            return touching
         
        if game.player.x <= self.x <= game.player.x + 40 and game.player.y <= self.y <= game.player.y + 80:
            touching = True
            game.player.lives -= 1

       return touching

    def despawn(self):
        game.projectiles.remove(self)


# Class to represent an enemy.
class Enemy:

    @staticmethod
    def spawn_new_line():
        if 1 in game.enemies_by_line.keys():
            game.lose()

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

    def despawn(self):
        del game.enemies[self.location]
        game.enemies_by_line[self.x / 50].remove(self)

        game.player.score += 1

        if len(game.enemies_by_line[self.x / 50]) < 1:
            del game.enemies_by_line[self.x / 50]

        if len(game.enemies_by_line.keys()) < 1 and len(game.enemies.keys()) < 1:
            game.next_round()


# Create a new game.
game = Game()

# Start the game if this module is run directly.
if __name__ == "__main__":
    game.start(pygame.display.set_mode((600, 600)))
