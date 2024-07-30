import pygame
from scripts.mapas.area1 import BG1
from scripts.mapas.area2 import BG2
from scripts.mapas.area3 import BG3
from scripts.mapas.area4 import BG4
from scripts.obj.obj import Obj
from scripts.obj.spaceship.spaceship import SpaceShip
from scripts.scene.scene import Scene
from scripts.settings import HEIGHT, WIDTH

class BG(Scene):
    
    def __init__(self) -> None:
        super().__init__()

        self.area = "area1"
        self.img = "assets/menu/espaco.png"
        self.pos = [0, 0]
        
        self.bg = BG1(self.img, self.pos, self.all_sprites)

        self.spaceship = SpaceShip("assets/nave1/nave100.png", [600, 600], self.all_sprites)
    def change(self):
        
       if self.area == "area1":
               if self.spaceship.rect.x < 0:
                self.area = "area2"
                self.spaceship.pos[0] = 1280 - self.spaceship.image.get_width()
                self.spaceship.pos[1] = self.spaceship.rect.y
                self.bg = BG2(self.img, self.pos, self.all_sprites)
                self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)
               elif self.spaceship.rect.y < 0:
                 self.area = "area4"
                 self.spaceship.pos[0] = self.spaceship.rect.x
                 self.spaceship.pos[1] = 720 - self.spaceship.image.get_height()
                 self.bg = BG4(self.img, self.pos, self.all_sprites)
                 self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)

       if self.area == "area2":
               if self.spaceship.rect.x > WIDTH - self.spaceship.image.get_width():
                self.area = "area1"
                self.spaceship.pos[0] = 0
                self.spaceship.pos[1] = self.spaceship.rect.y
                self.bg = BG1(self.img, self.pos, self.all_sprites)
                self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)
               elif self.spaceship.rect.y < 0:
                 self.area = "area3"
                 self.spaceship.pos[0] = self.spaceship.rect.x
                 self.spaceship.pos[1] = 720 - self.spaceship.image.get_width()
                 self.bg = BG3(self.img, self.pos, self.all_sprites)
                 self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)
        
       if self.area == "area3":
               if self.spaceship.rect.x > WIDTH - self.spaceship.image.get_width():
                self.area = "area4"
                self.spaceship.pos[0] = 0
                self.spaceship.pos[1] = self.spaceship.rect.y
                self.bg = BG4(self.img, self.pos, self.all_sprites)
                self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)
               elif self.spaceship.rect.y > HEIGHT - self.spaceship.image.get_width():
                 self.area = "area2"
                 self.spaceship.pos[0] = self.spaceship.rect.x + self.spaceship.image.get_width()
                 self.spaceship.pos[1] = 0
                 self.bg = BG2(self.img, self.pos, self.all_sprites)
                 self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)
       if self.area == "area4":
               if self.spaceship.rect.x < 0:
                self.area = "area3"
                self.spaceship.pos[0] = 1280
                self.spaceship.pos[1] = self.spaceship.rect.y
                self.bg = BG1(self.img, self.pos, self.all_sprites)
                self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)
               elif self.spaceship.rect.y > HEIGHT - self.spaceship.image.get_height():
                 self.area = "area1"
                 self.spaceship.pos[0] = self.spaceship.rect.x
                 self.spaceship.pos[1] = self.spaceship.image.get_height()
                 self.bg = BG1(self.img, self.pos, self.all_sprites)
                 self.spaceship = SpaceShip("assets/nave1/nave100.png", self.spaceship.pos, self.all_sprites)
            
       
    def update(self):
        self.draw()
        self.change()
        self.spaceship.update()

        
        


