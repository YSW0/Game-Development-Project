import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Walls(pygame.sprite.Sprite):
    def __init__(self):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.directions = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        self.direction = STOP
        self.color = YELLOW

        self.image = pygame.Surface([1000, 50])
        self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(0,100))
        
    
    def render(self, screen):
        
        screen.blit(self.image, (0, 0))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else