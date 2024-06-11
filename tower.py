import pygame

class Tower:
    def __init__(self, position):
        self.position = position
        self.range = 100
        self.damage = 10

    def update(self):
        # Logic to find and shoot at enemies
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.position, 20)
