import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Walls(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.color = WALL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites_surf = pygame.image.load('grass.jpg').convert()
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(self.sprites_surf, (0, 0))
        #self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    
    def render(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(self.sprites_surf, (0, 0))
        screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else
    
    