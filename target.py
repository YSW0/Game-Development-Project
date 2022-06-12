import pygame
from pygame.locals import *
from vector import Vector2
from constants import *
import numpy as np

class Target(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = PACMAN
        self.position = np.array([800, 384])
        self.directions = {STOP:np.array([0, 0]), UP:np.array([0, -1]), DOWN:np.array([0, 1]), LEFT:np.array([-1,0]), RIGHT:np.array([1,0])}
        self.direction = LEFT
        self.speed = 100
        self.radius = 10
        self.color = YELLOW
        
        self.step = 0
        

        #sprites_surf = pygame.image.load('MainGuySpriteSheet.png').convert()
        self.image = pygame.Surface([36, 36])
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        self.image.fill(YELLOW)
        #self.image.blit(sprites_surf, (0, 0), (0, 0, 36, 36))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        print(self.rect)


    def update(self, dt):	
        
        self.step = self.step + dt
        if 2 >= self.step % 5 > 1:
            self.direction = UP
        if 3 >= self.step % 5 > 2:
            self.direction = RIGHT
        if 4 >= self.step % 5 > 3:
            self.direction = DOWN
        else:
            self.direction = LEFT
        self.position += self.directions[self.direction]*(self.speed*dt)

    
    def render(self, screen):
        p = self.position
        self.rect = self.image.get_rect(center=p)

        #pygame.draw.circle(screen, self.color, p, self.radius) #Replace it with something else
        screen.blit(self.image, p)
