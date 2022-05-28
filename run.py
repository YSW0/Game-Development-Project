import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from Rect import Walls

class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
    
    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):
        self.setBackground()
        self.pacman = Pacman()
        self.wall = Walls()
        self.group = pygame.sprite.Group()
        self.group.add(self.wall)

    def update(self):
        dt = self.clock.tick() / 1000.0
        self.pacman.update(dt)
        self.checkEvents()
        pygame.sprite.spritecollide(self.pacman, self.group, True, collided=pygame.sprite.collide_mask)
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        self.pacman.render(self.screen)
        self.group.draw(self.screen)


        pygame.display.update()

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    
while True:
    game.update()