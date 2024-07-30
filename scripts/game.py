import pygame
from scripts.animations.explosion import Explosion
from scripts.mapas.mapa1 import BG
from scripts.obj.smallship import SmallShip
from scripts.obj.spaceship import SpaceShip
from scripts.scene.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Game(Scene): 

    def __init__(self):
        super().__init__()

        self.surface = pygame.display.get_surface()
        self.area = "area1"
        
        self.bg = BG()

        self.number = 100
        self.porcentagem = "%"
        self.text_demage = str(self.number) + self.porcentagem
        self.damage = Text("assets/fonts/airstrike.ttf",25,"Damage: ", "white", [30,30])
        self.p_text = Text("assets/fonts/airstrike.ttf", 25, self.text_demage, "white", [150, 30])

        self.tick = 0
        self.enemy_colision = pygame.sprite.Group()
        
        self.enemy_square = pygame.sprite.Group()
        
        self.powerups = pygame.sprite.Group()

        self.spaw()

        self.music = pygame.mixer.Sound("assets/sounds/bg.ogg")
        self.music.play(-1)
    
    def spaw(self):
        #self.tick += 1
        SmallShip("assets/nave/enemy0.png",[100, -3600], [self.all_sprites, self.enemy_colision])
        #self.tick = 0
    
    def change_map(self):
        
           if self.bg.area == "area1":
               if self.bg.spaceship.rect.x < 0:
                self.bg.area = "area2"
                self.bg.spaceship.rect.x = 1280
                self.bg.change()
               elif self.bg.spaceship.rect.y < 0:
                 self.bg.area = "area4"
                 self.bg.spaceship.rect.y = 720
                 self.bg.change()
            
           if self.bg.area == "area2":
               if self.bg.spaceship.rect.x  > WIDTH - self.bg.spaceship.image.get_width():
                self.bg.area = "area1"
                self.bg.spaceship.rect.x = 0
                self.bg.change()
               if self.bg.spaceship.rect.y < 0:
                 self.bg.area = "area3"
                 self.bg.spaceship.rect.y = 720
                 self.bg.change()
               
    def colision(self):
        for shot in self.bg.spaceship.shots:
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
        
        for powerup in self.powerups:
            if self.bg.spaceship.rect.colliderect(powerup.rect):
                powerup.kill()
                self.bg.spaceship.level += 1
                sound = pygame.mixer.Sound("assets/sounds/levelup.ogg")
                sound.play()

    def gameover(self):
        if self.bg.spaceship.damage <= 0:
            self.music.stop()
            self.active = False
                
    def update(self):
        self.bg.update()
        self.bg.spaceship.shots.draw(self.display)
        self.bg.spaceship.shots.update()
        self.colision()
        self.damage.draw()
        self.p_text.draw()
        self.gameover()
        return super().update()
        