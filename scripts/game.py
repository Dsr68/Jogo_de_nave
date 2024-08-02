import pygame
from scripts.animations.explosion import Explosion
from scripts.mapas.area1 import BG1
from scripts.mapas.area2 import BG2
from scripts.mapas.area3 import BG3
from scripts.mapas.area4 import BG4
from scripts.mapas.mapa1 import BG
from scripts.obj.smallship import SmallShip
from scripts.obj.spaceship.spaceship import SpaceShip
from scripts.scene.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Game(Scene): 

    def __init__(self):
        super().__init__()
    
        self.bg = BG()
        self.spaceship = SpaceShip("assets/nave1/nave100.png", [600, 600], self.all_sprites)

        self.number = 100
        self.text_demage = str(self.number) + " %"
        self.damage = Text("assets/fonts/airstrike.ttf",25,"Damage: ", "white", [30,30])
        self.p_text = Text("assets/fonts/airstrike.ttf", 25, self.text_demage, "white", [180, 30])

        self.number_fuel = self.spaceship.fuel
        self.fuel = Text("assets/fonts/airstrike.ttf",25,"Fuel: ", "white", [30,70])
        self.f_text = Text("assets/fonts/airstrike.ttf", 25, str(self.number_fuel) + " S", "white", [180, 70])

        self.storage = Text("assets/fonts/airstrike.ttf",25,"Storage: ", "white", [30,110])
        self.s_text = Text("assets/fonts/airstrike.ttf", 25, "5 Sg", "white", [180, 110])


        self.tick = 0
        self.enemy_colision = pygame.sprite.Group()

        self.music = pygame.mixer.Sound("assets/sounds/bg.ogg")
        self.music.play(-1)

    def change(self):
        
        self.number_fuel = self.spaceship.fuel
        self.f_text = Text("assets/fonts/airstrike.ttf", 25, "{:.2f}".format(self.number_fuel) + " S", "white", [180, 70])

    def change_map(self, spaceship):
        
       if self.bg.area == "area1":
               if spaceship.rect.x < 0:
                self.bg.area = "area2"
                spaceship.rect.x = 1280 - spaceship.image.get_width()
                spaceship.rect.y = spaceship.rect.y
                self.bg.bg = BG2("assets/menu/espaco.png", [0, 0], self.all_sprites)
               elif spaceship.rect.y < 0:
                 self.bg.area = "area4"
                 spaceship.rect.x = spaceship.rect.x
                 spaceship.rect.y = 720 - spaceship.image.get_height()
                 self.bg.bg = BG4("assets/menu/espaco.png", [0, 0], self.all_sprites)


       if self.bg.area == "area2":
               if spaceship.rect.x > WIDTH - spaceship.image.get_width():
                self.bg.area = "area1"
                spaceship.rect.x = 0
                spaceship.rect.y = spaceship.rect.y
                self.bg.bg = BG1("assets/menu/espaco.png", [0, 0], self.all_sprites)
               elif spaceship.rect.y < 0:
                 self.bg.area = "area3"
                 spaceship.rect.x = spaceship.rect.x
                 spaceship.rect.y = 720 - spaceship.image.get_width()
                 self.bg.bg = BG3("assets/menu/espaco.png", [0, 0], self.all_sprites)

        
       if self.bg.area == "area3":
               if spaceship.rect.x > WIDTH - spaceship.image.get_width():
                self.bg.area = "area4"
                spaceship.rect.x = 0
                spaceship.rect.y = spaceship.rect.y
                self.bg.bg = BG4("assets/menu/espaco.png", [0, 0], self.all_sprites)
               elif spaceship.rect.y > HEIGHT - spaceship.image.get_width():
                 self.bg.area = "area2"
                 spaceship.rect.x = spaceship.rect.x + spaceship.image.get_width()
                 spaceship.rect.y = 0
                 self.bg.bg = BG2("assets/menu/espaco.png", [0, 0], self.all_sprites)

       if self.bg.area == "area4":
               if spaceship.rect.x < 0:
                self.bg.area = "area3"
                spaceship.rect.x = 1280
                spaceship.rect.y = spaceship.rect.y
                self.bg.bg = BG1("assets/menu/espaco.png", [0, 0], self.all_sprites)
               elif spaceship.rect.y > HEIGHT - spaceship.image.get_height():
                 self.bg.area = "area1"
                 spaceship.rect.x = spaceship.rect.x
                 spaceship.rect.y = spaceship.image.get_height()
                 self.bg.bg = BG1("assets/menu/espaco.png", [0, 0], self.all_sprites)

               
    def colision(self):
        for shot in self.spaceship.shots:
            for enemy in self.enemy_colision:
                if shot.rect.colliderect(enemy.rect):
                    shot.kill()

                    sound = pygame.mixer.Sound("assets/sounds/block.ogg")
                    sound.play()

                    if enemy.life <= 0:
                        x = enemy.rect.x + enemy.image.get_width() / 2
                        y = enemy.rect.y + enemy.image.get_height() / 2
                        Explosion("assets/explosion/0.png",[x, y], [self.all_sprites])
        
        for enemy in self.enemy_colision:
            if self.bg.spaceship.rect.colliderect(enemy.rect):
                enemy.kill()
                self.bg.spaceship.damage -= 20
                self.number -= 20
                self.p_text.update_text(str(self.number)+"%")
                sound = pygame.mixer.Sound("assets/sounds/damage.ogg")
                sound.play()
        
        ''''for powerup in self.powerups:
            if self.bg.spaceship.rect.colliderect(powerup.rect):
                powerup.kill()
                self.bg.spaceship.level += 1
                sound = pygame.mixer.Sound("assets/sounds/levelup.ogg")
                sound.play()'''

    def gameover(self):
        if self.spaceship.damage <= 0:
            self.music.stop()
            self.active = False
                
    def update(self):
        self.bg.update()
        self.change_map(self.spaceship)
        self.change()
        self.colision()
        self.damage.draw()
        self.p_text.draw()
        self.fuel.draw()
        self.f_text.draw()
        self.storage.draw()
        self.s_text.draw()
        self.gameover()
        return super().update()
        