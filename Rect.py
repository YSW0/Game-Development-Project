import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Bush(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 70, height = 130):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.color = WALL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites_surf = pygame.image.load('bush.png').convert()
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.blit(self.sprites_surf, (0, 0))
        self.image.set_colorkey((0, 0, 0))
        #self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    
    def render(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.blit(self.sprites_surf, (0, 0))
        screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else

class Bound(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.color = WALL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        #self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    
    def render(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.blit(self.sprites_surf, (0, 0))
        screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else

class Statues(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 100, height = 294):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.color = WALL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites_surf = pygame.image.load('statues.png').convert()
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image.blit(self.sprites_surf, (0, 0))
        self.image.set_colorkey((0, 0, 0))
        #self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    
    def render(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.blit(self.sprites_surf, (0, 0))
        screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else

class Wall1(pygame.sprite.Sprite):
    def __init__(self, x, y, width=260, height=237):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.color = WALL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sprites_surf = pygame.image.load('wall1.png').convert()
        self.image.blit(self.sprites_surf, (0, 0))
        self.image.set_colorkey((0, 0, 0))
        #self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    
    def render(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.blit(self.sprites_surf, (0, 0))
        screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else


class Wall2(pygame.sprite.Sprite):
    def __init__(self, x, y, width=40, height=163):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.color = WALL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sprites_surf = pygame.image.load('wall2.png').convert()
        self.image.blit(self.sprites_surf, (0, 0))
        self.image.set_colorkey((0, 0, 0))
        #self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    
    def render(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.blit(self.sprites_surf, (0, 0))
        screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else



class Wall4(pygame.sprite.Sprite):
    def __init__(self, x, y, width=186, height=444):
        self.name = PACMAN
        pygame.sprite.Sprite.__init__(self)
        self.color = WALL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sprites_surf = pygame.image.load('wall4.png').convert()
        self.image.blit(self.sprites_surf, (0, 0))
        self.image.set_colorkey((0, 0, 0))
        #self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    
    def render(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.blit(self.sprites_surf, (0, 0))
        screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
        #pygame.draw.rect(screen, self.color, rect) #Replace it with something else