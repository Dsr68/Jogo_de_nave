import random
from view.text import Text
from view.config import *
import pygame
from view.obj import Obj
from view.spaceship import SpaceShip

class Game():

    def __init__(self):
        super().__init__()

        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/menu/espaco.png",[0,0],[0,-720],[self.all_sprites])
        self.spaceship = SpaceShip("assets/nave1/nave100.png",[600,600],[self.all_sprites])

        self.pts = 0
        self.score_text = Text("assets/fonts/airstrike.ttf",25,"Score: ", "white", [30,30])
        self.score_pts = Text("assets/fonts/airstrike.ttf",25, "0" , "white", [130,30])

        self.tick = 0
        self.enemy_colision = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.music = pygame.mixer.Sound("assets/sounds/bg.ogg")
        self.music.play(-1)

    def colision(self):
        for shot in self.spaceship.shots:
            for enemy in self.enemy_colision:
                if shot.rect.colliderect(enemy.rect):
                    shot.kill()
                    enemy.life -= 1
                    self.pts += 1
                    self.score_pts.update_text(str(self.pts))

                    sound = pygame.mixer.Sound("assets/sounds/block.ogg")
                    sound.play()

                    if enemy.life <= 0:
                        x = enemy.rect.x + enemy.image.get_width() / 2
                        y = enemy.rect.y + enemy.image.get_height() / 2
                        Explosion("assets/explosion/0.png",[x, y], [self.all_sprites])
        
        for enemy in self.enemy_colision:
            if self.spaceship.rect.colliderect(enemy.rect):
                enemy.kill()
                self.spaceship.life -= 1
                self.spaceship.level = 1
                sound = pygame.mixer.Sound("assets/sounds/damage.ogg")
                sound.play()
        
        for powerup in self.powerups:
            if self.spaceship.rect.colliderect(powerup.rect):
                powerup.kill()
                self.spaceship.level += 1
                sound = pygame.mixer.Sound("assets/sounds/levelup.ogg")
                sound.play()

    def gameover(self):
        if self.spaceship.life <= 0:
            self.music.stop()
            self.active = False
                
    def update(self):
        self.spaceship.shots.draw(self.display)
        self.spaceship.shots.update()
        #self.colision()
        self.bg.update()
        #self.spaceship.input()
        #self.spaw_enemy()
        #self.score_text.draw()
        #self.score_pts.draw()
        #self.gameover()
        #self.hud()'''
        return super().update()


class Shot():

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 5
    
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y < -100:
            self.kill()

class Enemy():

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 1
        self.life = 1
    
    def destruction(self):
        if self.life <= 0:
            self.kill()
    
    def limits(self):
        if self.rect.y > RIGHT + self.image.get_height():
            self.kill()
    
    def move(self):
        self.rect.y += self.speed

    def update(self):
        self.destruction()
        self.limits()
        self.move()
        
class SmallShip(Enemy):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 6
        self.life = 1
    
    def update(self):
        self.animation(8,3,"assets/nave/enemy")
        return super().update()

class MediumShip(Enemy):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)


        self.speed = 4
        self.life = 2
    
    def update(self):
        self.animation(8,3,"assets/nave/enemy2_")
        return super().update()

class BigShip(Enemy):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 1
        self.life = 10
    
    def update(self):
        self.animation(16,3,"assets/nave/enemy3_")
        return super().update()

class PowerUp(Enemy):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 2
    
    def update(self):
        self.animation(16,3,"assets/nave/powerup")
        return super().update()

class Explosion(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.ticks = 0
    
    def update(self):
        self.animation(5,5,"assets/explosion/")

        self.ticks += 1
        if self.ticks > 25:
            self.kill()
        return super().update()