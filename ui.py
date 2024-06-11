import pygame

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        text = self.font.render("Tower Defense Game", True, (255, 255, 255))
        screen.blit(text, (10, 10))
