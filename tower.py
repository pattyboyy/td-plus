import pygame
from projectile import Projectile

class Tower:
    def __init__(self, position, game):
        self.position = position
        self.range = 150
        self.game = game
        self.projectiles = []
        self.damage = 10

    def update(self):
        # Logic to find and shoot at enemies
    def update(self, screen):
        # Logic to find and shoot at enemies
        for enemy in self.game.enemies:
            if self.in_range(enemy):
                self.shoot(enemy, screen)

        for projectile in self.projectiles:
            projectile.update()
            projectile.draw(screen)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.position, 20)
    def in_range(self, enemy):
        distance = ((self.position[0] - enemy.position[0]) ** 2 + (self.position[1] - enemy.position[1]) ** 2) ** 0.5
        return distance <= self.range

    def shoot(self, enemy, screen):
        projectile = Projectile(self.position, enemy)
        self.projectiles.append(projectile)
        projectile = Projectile(self.position, enemy)
        self.projectiles.append(projectile)
