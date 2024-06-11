import pygame

class Enemy:
    def __init__(self, path):
        self.path = path
        self.position = path.start
        self.health = 100
        self.speed = 2

    def update(self):
        # Logic to move along the path
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, 10)
