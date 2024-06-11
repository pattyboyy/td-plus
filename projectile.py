import pygame

class Projectile:
    def __init__(self, position, target):
        self.position = position
        self.target = target
        self.speed = 5

    def update(self):
        # Logic to move towards the target
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, 5)
