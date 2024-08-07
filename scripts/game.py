import pygame
from scripts.animations.animationMap import AnimationMap
from scripts.bases.enemy import Enemy
from scripts.nave.spaceship import Spaceship
from scripts.bases.scene import Scene
from scripts.settings import HEIGHT, WIDTH

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimationMap("assets/menu/espaco.png", self.all_sprites)
        self.spaceship = Spaceship("assets/nave1/up/nave100.png", self.bg, [600, 600], self.all_sprites)

        self.enemy_colision = pygame.sprite.Group()
        Enemy("assets/nave/enemy0.png", [600, 0], [self.all_sprites, self.enemy_colision])

    def colision(self):

        for shot in self.spaceship.tiros:
            for enemy in self.enemy_colision:
                if shot.rect.colliderect(enemy.rect):
                    shot.kill()
                    enemy.life -= 1

        for enemy in self.enemy_colision:
            if self.spaceship.rect.colliderect(enemy.rect):
                enemy.kill()
                self.spaceship.v_demange -= 20
                self.spaceship.format_demage = str(self.spaceship.v_demange)
                self.spaceship.demage_valor.update(self.spaceship.format_demage+"%")
                print(self.spaceship.life)

    def gameover(self):

        if self.life <= 0:
            self.active = False


    def update(self):
        self.spaceship.input()
        self.spaceship.tiros.draw(self.display)
        self.spaceship.tiros.update()
        self.colision()
        
        return super().update()