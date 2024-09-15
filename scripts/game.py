import pygame
from scripts.animations.animationMap import AnimationMap
from scripts.bases.enemy import Enemy
from scripts.bases.obj import Obj
from scripts.nave.spaceship import Spaceship
from scripts.bases.scene import Scene
from scripts.settings import HEIGHT, WIDTH
from scripts.text import Text

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimationMap("assets/menu/espaco.png", self.all_sprites)
        self.spaceship = Spaceship("assets/nave1/up/nave100.png", self.bg, [600, 600], self.all_sprites)

        self.format_demange = str(self.spaceship.demange)
        self.demange = Text("assets/fonts/airstrike.ttf", 25, "Damage", "white", [30, 30])
        self.demange_valor = Text("assets/fonts/airstrike.ttf", 25, self.format_demange + "%", "white", [160, 30])

        self.format_fuel = str(self.spaceship.fuel)
        self.fuel = Text("assets/fonts/airstrike.ttf", 25, "Fuel", "white", [30, 60])
        self.fuel_valor = Text("assets/fonts/airstrike.ttf", 25, self.format_fuel, "white", [160, 60])

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
                self.spaceship.demange -= 20
                self.format_demange = str(self.spaceship.demange)
                self.demange_valor.update(self.format_demange+"%")
                print(self.spaceship.life)

        for estacao in self.bg.estacoes:
                if self.spaceship.rect.colliderect(estacao):
                    self.spaceship.abastecer()


    def gameover(self):

        if self.life <= 0:
            self.active = False


    def update(self):
        self.demange.draw()
        self.demange_valor.draw()
        self.fuel.draw()
        self.fuel_valor.draw()
        self.fuel_valor.update(f'{self.spaceship.fuel: .2f}')
        self.spaceship.input()
        self.spaceship.tiros.draw(self.display)
        self.spaceship.tiros.update()
        self.colision()
                
        return super().update()