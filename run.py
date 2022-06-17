import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from pacmanLevel2 import PacmanSecond
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
        self.background.fill((BLACK))

    def startGame(self):
        self.f = open("record.txt", "a")
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
        dt = self.clock.tick() / 1000.0
        self.checkEvents()
                
        
        if pygame.sprite.spritecollide(self.pacman, self.group, False, collided=pygame.sprite.collide_rect_ratio(1)):
            #self.f.write(self.pacman.rect.__str__())
            #print(self.pacman.rect)
            if self.pacman.direction == UP:             #Used to be self.pacman.getValidKey(). It is noted that key press and direction were not necessarily in sync. ie:: we got no Ket press, but the man can walk following previous miliseconds key press!
                self.pacman.directions[UP] = Vector2(0, 0)
                #self.pacman.directions[UP] = np.array([0, 0])
                self.pacman.position -= Vector2(0, -1)#np.array([0, -1])
            if self.pacman.direction == DOWN:
                self.pacman.directions[DOWN] = Vector2(0, 0)
                #self.pacman.directions[DOWN] = np.array([0, 0])
                self.pacman.position -= Vector2(0, 1)#np.array([0, 1])
            if self.pacman.direction == LEFT:
                self.pacman.directions[LEFT] = Vector2(0, 0)
                #self.pacman.directions[LEFT] = np.array([0, 0])
                self.pacman.position += Vector2(1, 0)#np.array([1, 0])
                #self.f.write('right + 5')
                #print('right + 5')
            if self.pacman.direction == RIGHT:
                self.pacman.directions[RIGHT] = Vector2(0, 0)
                #self.pacman.directions[RIGHT] = np.array([0, 0])
                self.pacman.position += Vector2(-1, 0)#np.array([-1, 0])
        else:
            self.pacman.directions = {STOP:Vector2(0, 0), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}#{STOP:np.array([0, 0]), UP:np.array([0, -1]), DOWN:np.array([0, 1]), LEFT:np.array([-1,0]), RIGHT:np.array([1,0])}#
            
       
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
            self.pacman.image.blit(sprites_surf, (0, 0), (0, 124, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (42, 124, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (84, 124, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()

        if self.pacman.getValidKey() == LEFT:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacman.image.blit(sprites_surf, (0, 0), (0, 43, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (42, 43, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (84, 43, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()

        if self.pacman.getValidKey() == RIGHT:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacman.image.blit(sprites_surf, (0, 0), (0, 83, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (42, 83, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()
            self.pacman.image.blit(sprites_surf, (0, 0), (84, 83, 36, 42))
            self.pacman.render(self.screen)
            pygame.display.update()

            
        self.pacman.update(dt)
        self.target.update(dt)

#self.wall.update(dt)
        direction = self.pacman.getValidKey()
        self.pacman.direction = direction
        for wall in self.group:
            wall.x -= (self.pacman.directions[self.pacman.direction].x)*(self.pacman.speed*dt)
            wall.y -= (self.pacman.directions[self.pacman.direction].y)*(self.pacman.speed*dt)
        self.target.position -= self.pacman.directions[self.pacman.direction] * self.pacman.speed*dt
        


        self.render()
    
    def secondUpdate(self):
        dt = self.clock.tick() / 1000.0
        self.checkEvents()
        if self.pacmanSecond.getValidKey() == DOWN:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (0, 0, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (42, 0, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (84, 0, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
        
        if self.pacmanSecond.getValidKey() == UP:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (0, 124, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (42, 124, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (84, 124, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()

        if self.pacmanSecond.getValidKey() == LEFT:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (0, 43, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (42, 43, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (84, 43, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()

        if self.pacmanSecond.getValidKey() == RIGHT:
            sprites_surf = pygame.image.load('hdhd.png').convert()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (0, 83, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (42, 83, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
            self.pacmanSecond.image.blit(sprites_surf, (0, 0), (84, 83, 36, 42))
            self.pacmanSecond.render(self.screen)
            pygame.display.update()
        self.pacmanSecond.update(dt)
        self.screen.blit(self.background, (0, 0))
        self.pacmanSecond.render(self.screen)
        pygame.display.update()

    def secondScene(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill((BLACK))
        self.pacmanSecond = PacmanSecond()
        pygame.display.update()



    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.f.close()
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        self.pacman.render(self.screen)
        self.target.render(self.screen)
        for element in self.group:
            element.render(self.screen)
        #self.group.draw(self.screen)
    


        pygame.display.update()

        

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    
while True:
    game.update()
    lim = 260
    if pygame.key.get_pressed()[K_1]:
        while game.wall_1.height < lim:
            pygame.time.delay(1)
            for element in game.group:
                element.x = element.x*1.001
                element.y = element.y*1.001
                element.width = element.width*1.001
                element.height = element.height*1.001
            game.target.position = game.target.position*1.001
            game.update()
    
    if pygame.sprite.collide_rect(game.pacman, game.target):
        break

game.secondScene()

while True:
    game.secondUpdate()
    