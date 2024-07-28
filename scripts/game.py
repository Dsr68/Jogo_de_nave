import pygame
from scripts.animations.animacaobg import AnimacaoBG
from scripts.animations.explosion import Explosion
from scripts.obj.smallship import SmallShip
from scripts.obj.spaceship import SpaceShip
from scripts.obj.square import Square
from scripts.scene.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Game(Scene): 

    def __init__(self):
        super().__init__()

        self.surface = pygame.display.get_surface()
        self.bg = AnimacaoBG("assets/menu/espaco.png", [0,0], [0, -720], [self.all_sprites])
        self.bg.draw_radar()
        
        self.spaceship = SpaceShip("assets/nave1/nave100.png",[600,600],[self.all_sprites])

        self.number = 100
        self.porcentagem = "%"
        self.text_demage = str(self.number) + self.porcentagem
        self.damage = Text("assets/fonts/airstrike.ttf",25,"Damage: ", "white", [30,30])
        self.p_text = Text("assets/fonts/airstrike.ttf", 25, self.text_demage, "white", [150, 30])

        self.tick = 0
        self.enemy_colision = pygame.sprite.Group()
        
        self.enemy_square = pygame.sprite.Group()
        
        self.powerups = pygame.sprite.Group()

        self.spaw_enemy()

        self.music = pygame.mixer.Sound("assets/sounds/bg.ogg")
        self.music.play(-1)
    
    def spaw_enemy(self):
        #self.tick += 1
        enemy = SmallShip("assets/nave/enemy0.png",[100, -3600], [self.all_sprites, self.enemy_colision])
        Square("assets/square/square0.png", enemy.rect,)
        #self.tick = 0

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
            if self.spaceship.rect.colliderect(enemy.rect):
                enemy.kill()
                self.spaceship.damage -= 20
                self.number -= 20
                self.p_text.update_text(str(self.number)+"%")
                sound = pygame.mixer.Sound("assets/sounds/damage.ogg")
                sound.play()
        
        for powerup in self.powerups:
            if self.spaceship.rect.colliderect(powerup.rect):
                powerup.kill()
                self.spaceship.level += 1
                sound = pygame.mixer.Sound("assets/sounds/levelup.ogg")
                sound.play()

    def gameover(self):
        if self.spaceship.damage <= 0:
            self.music.stop()
            self.active = False
                
    def update(self):
        self.spaceship.shots.draw(self.display)
        self.spaceship.shots.update()
        self.colision()
        #self.bg.update()
        self.spaceship.input()
        self.damage.draw()
        self.p_text.draw()
        self.gameover()
        return super().update()
        