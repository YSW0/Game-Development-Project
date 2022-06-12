import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from Rect import Walls
from target import Target
from vector import Vector2
import numpy as np

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
        self.target = Target()
        self.wall_1 = Walls(200, 192, 130, 130) #centerx, centery, width, height
        self.wall_2 = Walls(200, 600, 130, 130)
        self.wall_3 = Walls(200, 400, 130, 130)
        self.wall_4 = Walls(490, 300, 50, 400)
        self.wall_5 = Walls(520, 550, 400, 50)
        self.wall_6 = Walls(670, 150, 200, 200)
        self.group = pygame.sprite.Group()
        self.group.add(self.wall_1)
        self.group.add(self.wall_2)
        self.group.add(self.wall_3)
        self.group.add(self.wall_4)
        self.group.add(self.wall_5)
        self.group.add(self.wall_6)

    def update(self):
        dt = 1 #self.clock.tick() / 900.0
        
        self.checkEvents()
        if pygame.sprite.spritecollide(self.pacman, self.group, False, collided=pygame.sprite.collide_rect):
            if self.pacman.getValidKey() == UP:
                self.pacman.directions[UP] = np.array([0, 0])
                self.pacman.position -= np.array([0, -1])
            if self.pacman.getValidKey() == DOWN:
                self.pacman.directions[DOWN] = np.array([0, 0])
                self.pacman.position -= np.array([0, 1])
            if self.pacman.getValidKey() == LEFT:
                self.pacman.directions[LEFT] = np.array([0, 0])
                self.pacman.position += np.array([1, 0])
            if self.pacman.getValidKey() == RIGHT:
                self.pacman.directions[RIGHT] = np.array([0, 0])
                self.pacman.position += np.array([-1, 0])
        
       
        if self.pacman.getValidKey() == DOWN:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacman.image.blit(sprites_surf, (0, 0), (0, 0, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (42, 0, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (84, 0, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
        
        if self.pacman.getValidKey() == UP:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacman.image.blit(sprites_surf, (0, 0), (0, 124, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (42, 124, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (84, 124, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()

        if self.pacman.getValidKey() == LEFT:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacman.image.blit(sprites_surf, (0, 0), (0, 42, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (42, 42, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (84, 42, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()

        if self.pacman.getValidKey() == RIGHT:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacman.image.blit(sprites_surf, (0, 0), (0, 83, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (42, 83, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (84, 83, 36, 45))
            self.pacman.render(self.screen)
            pygame.display.update()


            
        

        else:
            self.pacman.directions = {STOP:np.array([0, 0]), UP:np.array([0, -1]), DOWN:np.array([0, 1]), LEFT:np.array([-1,0]), RIGHT:np.array([1,0])}#{STOP:Vector2(0, 0), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
            
        self.pacman.update(dt)
        self.target.update(dt)
        
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        self.pacman.render(self.screen)
        self.target.render(self.screen)
        self.group.draw(self.screen)


        pygame.display.update()

        

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    
while True:
    game.update()