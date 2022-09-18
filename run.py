import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from pacmanLevel2 import PacmanSecond
from Rect import Bush, Wall1, Wall4
from Rect import Wall2
from Rect import Bound
from Rect import Statues
from target import Target
from vector import Vector2
import numpy as np

class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.flagg = False
        pygame.mixer.init()
        self.walk_sound = pygame.mixer.Sound('steps.ogg')
        self.target_sound = pygame.mixer.Sound('003.mp3')
        self.walk_sound.set_volume(1)
        self.bgm = pygame.mixer.Sound('GameBGM.mp3')
        self.bgm.set_volume(0.1)
        self.bgm.play()
        
        
    
    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill((BLACK))
        self.bi = pygame.image.load('Day.png').convert()
        self.blk = pygame.image.load('Black.jpg').convert()
        self.bix = 0
        self.biy = 0
        self.fil = pygame.image.load('fill.png').convert()
        self.filter = False
        self.filterx = 0
        self.filtery = 0
        self.background.blit(self.bi, (self.bix, self.biy))

    def startGame(self):
        #self.target_sound.play()
        self.f = open("record.txt", "a")
        self.setBackground()
        self.pacman = Pacman()
        self.target = Target()
        self.wall_1 = Bush(200, 360) #centerx, centery, width, height
        self.wall_2 = Bush(200, 760)
        self.wall_3 = Bush(200, 960)
        self.wall_4 = Wall2(350, 450)
        self.wall_5 = Wall2(350, 682)
        self.wall_12 = Wall2(350, 915)
        self.wall_6 = Bound(500, 220, 2000, 10)
        self.wall_7 = Bound(0, 384, 10, 2000)
        self.wall_8 = Statues(1260, 500)
        self.wall_9 = Wall1(600, 850)
        self.wall_10 = Wall1(865, 850)
        self.wall_11 = Wall1(1130, 850)
        self.wall_13 = Wall4(900, 350)
        self.wall_14 = Wall4(900, 500)
        self.wall_17 = Wall4(1430, 800)
        self.wall_18 = Wall2(200, 560)
        self.wall_19 = Bound(500, 1124, 2000, 10)
        self.wall_20 = Bound(1500, 384, 10, 2000)
        '''
        self.wall_2 = Walls(200, 600, 130, 130)
        self.wall_3 = Walls(200, 400, 130, 130)
        self.wall_4 = Walls(490, 300, 50, 400)
        self.wall_5 = Walls(520, 550, 400, 50)
        self.wall_6 = Walls(670, 150, 200, 200)
        '''
        self.group = pygame.sprite.Group()
        self.group.add(self.wall_1)
        self.group.add(self.wall_2)
        self.group.add(self.wall_3)
        self.group.add(self.wall_4)
        self.group.add(self.wall_5)
        self.group.add(self.wall_6)
        self.group.add(self.wall_7)
        self.group.add(self.wall_8)
        self.group.add(self.wall_9)
        self.group.add(self.wall_10)
        self.group.add(self.wall_11)
        self.group.add(self.wall_12)
        self.group.add(self.wall_13)
        self.group.add(self.wall_14)
        self.group.add(self.wall_17)
        self.group.add(self.wall_18)
        self.group.add(self.wall_19)
        self.group.add(self.wall_20)
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
            
       
        if self.pacman.getValidKey() == DOWN and self.flagg == True:
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
        
        if self.pacman.getValidKey() == UP and self.flagg == True:
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

        if self.pacman.getValidKey() == LEFT and self.flagg == True:
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

        if self.pacman.getValidKey() == RIGHT and self.flagg == True:
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
        if self.flagg == True:
            direction = self.pacman.getValidKey()
            self.pacman.direction = direction
            for wall in self.group:
                wall.x -= (self.pacman.directions[self.pacman.direction].x)*(self.pacman.speed*dt)
                wall.y -= (self.pacman.directions[self.pacman.direction].y)*(self.pacman.speed*dt)
            self.target.position -= self.pacman.directions[self.pacman.direction] * self.pacman.speed*dt
            '''
            for wall in self.group:
                if self.bix < 50:
                    wall.x -= (self.pacman.directions[self.pacman.direction].x)*(self.pacman.speed*dt)
                
                else:
                    wall.x -= 1
                    #self.target.position.x -= 1
                if self.biy < 140:
                    wall.y -= (self.pacman.directions[self.pacman.direction].y)*(self.pacman.speed*dt)
                    
                else:
                    wall.y -= 1
                    #self.target.position.y -= 1
            if self.bix < 50 and self.biy < 140:
                self.target.position -= self.pacman.directions[self.pacman.direction] * self.pacman.speed*dt
            elif self.bix < 50:
                self.target.position.y -= 1
            elif self.biy < 140:
                self.target.position.x -= 1
            '''
            self.background.blit(self.blk, (self.bix, self.biy))

            self.bix -= (self.pacman.directions[self.pacman.direction].x)*(self.pacman.speed*dt)
            self.biy -= (self.pacman.directions[self.pacman.direction].y)*(self.pacman.speed*dt)
            self.filx = self.bix
            self.fily = self.biy

            self.background.blit(self.bi, (self.bix, self.biy))
            if self.filter == True:
                self.background.blit(self.fil, (self.filx, self.fily))
            else:
                self.background.blit(self.bi, (self.bix, self.biy))

            '''
            if self.bix < 50:
                self.bix -= (self.pacman.directions[self.pacman.direction].x)*(self.pacman.speed*dt)
            else:
                self.bix -= 1
            if self.biy < 140:
                self.biy -= (self.pacman.directions[self.pacman.direction].y)*(self.pacman.speed*dt)
            else:
                self.biy -= 1
            self.background.blit(self.bi, (self.bix, self.biy))
            '''
            
        

        self.render()
    '''
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
    '''
    def secondScene(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill((BLACK))
        fontobj = setup_fonts(36)
        wrapped_rect = pygame.Rect(0, 0, 1024, 768)
        wrapped_surface = word_wrap(wrapped_rect, fontobj, (255, 255, 255), "Well done, you did it! Click 'x' to exit.")
        self.screen.blit(wrapped_surface, wrapped_rect)
        pygame.draw.rect(self.screen, (0,0,0), wrapped_rect, width=1)
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

        pygame.display.flip()
    
def word_wrap(rect, font, color, text):

    size = w, h = rect.size
    surf = pygame.Surface(size, pygame.SRCALPHA, 32)
    surf = surf.convert_alpha()
    x = 0
    y = 0
    for char in text:
        text_surface = font.render(char, True, color)
        width, height = text_surface.get_size()
        if x + width >= w:
            y = y + height
            x = 0
        if y + height > h:
            break
        surf.blit(text_surface, (x, y))
        x = x + width
        
    return surf
    
def setup_fonts(font_size, bold=False, italic=False):
    

    font_preferences = ['Helvetica Neue', 'Iosevka Regular', 'Comic Sans', 'Courier New']
    available = pygame.font.get_fonts()
    prefs = [x.lower().replace(' ', '') for x in font_preferences]
    for pref in prefs:
        a = [x
            for x in available
            if x.startswith(pref)
            ]
        if a:
            fonts = ','.join(a) #SysFont expects a string with font names in it
            return pygame.font.SysFont(fonts, font_size, bold, italic)
    return pygame.font.SysFont(None, font_size, bold, italic)
        

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    #game.update()
    

timer = 0
while True:
    game.checkEvents()
    timer += 1
    fontobj = setup_fonts(36)
    wrapped_rect = pygame.Rect(0, 0, 1024, 768)
    wrapped_surface = word_wrap(wrapped_rect, fontobj, (255, 255, 255), "After the text disappears, press '1' to start. Go Find The Yellow Box. Go night with key 'n'. To return the day, use key 'd'.")
    game.screen.blit(wrapped_surface, wrapped_rect)
    pygame.draw.rect(game.screen, (0,0,0), wrapped_rect, width=1)
    pygame.display.update()
    if timer > 650:
        break
enter = False

while True:

    game.update()

    if pygame.key.get_pressed()[K_1]:
        game.flagg = True
    if pygame.key.get_pressed()[K_n]:
        game.filter = True
    if pygame.key.get_pressed()[K_d]:
        game.filter = False
    '''
    distance = (game.target.position.x - game.pacman.position.x)*(game.target.position.x - game.pacman.position.x) + (game.target.position.y - game.pacman.position.y)*(game.target.position.y - game.pacman.position.y)
    if distance > 1000:
        game.target_sound.set_volume(0.1)
    elif distance > 700 and distance <= 1000:
        game.target_sound.set_volume(0.4)
    elif distance > 400 and distance <= 700:
        game.target_sound.set_volume(0.7)
    elif distance > 100 and distance <= 400:
        game.target_sound.set_volume(0.8)
    elif distance > 0 and distance <=100:
        game.target_sound.set_volume(1)
    game.target_sound.play()
    
    lim = 260
    if pygame.key.get_pressed()[K_1]:
        game.flagg = True
        while game.wall_1.height < lim:
            pygame.time.delay(1)
            for element in game.group:
                element.x = element.x*1.001
                element.y = element.y*1.001
                element.width = element.width*1.001
                element.height = element.height*1.001
            game.target.position = game.target.position*1.001
            game.update()
    '''
    if pygame.sprite.collide_rect(game.pacman, game.target):
        game.walk_sound.stop()
        game.bgm.stop()
        break
    if enter == True:
        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_DOWN] or pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_RIGHT]:
            if game.flagg == True:
                game.walk_sound.play()
                enter = False
    else:
        game.walk_sound.stop()
        enter = True
    
    if not pygame.mixer.get_busy():
        game.bgm.play()
        
        
while True:
    game.checkEvents()
    game.secondScene()
    