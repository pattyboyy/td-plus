import pygame
from tower import Tower
from enemy import Enemy
from path import Path
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tower Defense Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.towers = []
        self.enemies = []
        self.path = Path()
        self.ui = UI()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for tower in self.towers:
            tower.update()
        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.path.draw(self.screen)
        for tower in self.towers:
            tower.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.ui.draw(self.screen)
        pygame.display.flip()
