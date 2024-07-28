import pygame
from scripts.obj.obj import Obj
from scripts.settings import *

class Scene:

    def __init__(self) -> None:
        
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.active = True

        self.fade = Fade(5)

    def events(self, event):
        pass

    def draw(self):
        self.all_sprites.draw(self.display)

    def update(self):
        self.fade.draw()
        self.all_sprites.update()

class Fade:

    def __init__(self, speed) -> None:
        
        self.display = pygame.display.get_surface()
        self.surface = pygame.Surface([WIDTH, HEIGHT]).convert_alpha()
        self.surface.fill("black")

        self.alfa = 255
        self.speed = speed

    def draw(self):

        if self.alfa > 0:
            self.alfa -= self.speed

        self.surface.set_alpha(self.alfa)
        self.display.blit(self.surface, [0,0])
