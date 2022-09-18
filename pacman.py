import pygame
from pygame.locals import *
from vector import Vector2
from constants import *
import numpy as np

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = PACMAN
        #self.position = np.array([50, 384])

        self.position = Vector2(50, 384)

        #self.directions = {STOP:np.array([0, 0]), UP:np.array([0, -1]), DOWN:np.array([0, 1]), LEFT:np.array([-1,0]), RIGHT:np.array([1,0])}
        self.directions = {STOP:Vector2(0, 0), UP:Vector2(0, -1), DOWN:Vector2(0, 1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        self.direction = STOP
        self.speed = 150
        self.radius = 10
        self.color = YELLOW
        
        sprites_surf = pygame.image.load('hdhd.png').convert()

        self.image = pygame.Surface([36, 42])
        #self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
        self.image.blit(sprites_surf, (0, 0), (0, 0, 36, 42))
        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        #self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        #print(self.rect)


    def update(self, dt):	
        '''
        direction = self.getValidKey()
        self.direction = direction
        self.position += self.directions[self.direction]*(self.speed*dt)
        '''
        

    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            #self.ff = open("record.txt", "a")
            #self.ff.write("walk left 1")
            #print('walk left 1')
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP
    
    def render(self, screen):
        p = self.position.asInt()
        self.rect = self.image.get_rect(center=p)

        #pygame.draw.circle(screen, self.color, p, self.radius) #Replace it with something else
        screen.blit(self.image, (p[0]-18, p[1]-21))

    


    