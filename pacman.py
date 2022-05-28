import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = PACMAN
        self.position = Vector2(200, 400)
        self.directions = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        self.direction = STOP
        self.speed = 100
        self.radius = 10
        self.color = YELLOW
        
        self.image = pygame.Surface([self.radius*2, self.radius*2])
        self.image.fill(self.color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(200, 400))


    def update(self, dt):	
        direction = self.getValidKey()
        self.direction = direction
        self.position += self.directions[self.direction]*self.speed*dt

    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP
    
    def render(self, screen):
        p = self.position.asInt()
        self.rect = self.image.get_rect(center=p)

        #pygame.draw.circle(screen, self.color, p, self.radius) #Replace it with something else
        screen.blit(self.image, p)

    


    