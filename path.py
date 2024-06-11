import pygame

class Path:
    def __init__(self):
        self.start = (50, 50)
        self.end = (750, 550)
        self.points = [(50, 50), (750, 550)]

    def draw(self, screen):
        pygame.draw.lines(screen, (255, 255, 255), False, self.points, 5)
