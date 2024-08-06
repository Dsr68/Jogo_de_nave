import pygame

from scripts.bases.obj import Obj
from scripts.settings import HEIGHT, WIDTH
from scripts.text import Text


class Spaceship(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.life = 3

        self.tiros = pygame.sprite.Group()
        self.ticks = 0

        self.v_demange = 100.00
        self.demage = Text("assets/fonts/airstrike.ttf", 25, "Damage", "white", [30, 30])
        self.demage_valor = Text("assets/fonts/airstrike.ttf", 25, str(self.v_demange) + "%", "white", [160, 30])

        self.v_fuel = 100
        self.fuel = Text("assets/fonts/airstrike.ttf", 25, "Fuel", "white", [30, 60])
        self.fuel_valor = Text("assets/fonts/airstrike.ttf", 25, str(self.v_fuel), "white", [160, 60])

    def input(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction.y = -1
            self.cosume()    
        elif key[pygame.K_s]:
            self.direction.y = 1
            self.cosume()
        else:
            self.direction.y = 0

        if key[pygame.K_a]:
            self.direction.x = -1
            self.cosume()
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.cosume()
        else:
            self.direction.x = 0

        click = pygame.mouse.get_pressed()

        if click[0] == True:
            self.ticks += 1
            
            if self.ticks == 1:
                Shot("assets/tiro1/tiro1.png", [self.rect.x, self.rect.y-20], self.tiros)

            elif self.ticks > 30:
                self.ticks = 0
                Shot("assets/tiro1/tiro1.png", [self.rect.x, self.rect.y-20], self.tiros)

    def move(self):
        self.rect.center += self.direction * self.speed

    def limit(self):

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.image.get_width():
            self.rect.x = WIDTH - self.image.get_width()

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT- self.image.get_width():
            self.rect.y = HEIGHT- self.image.get_width()

    def cosume(self):

        if self.v_fuel > 0:
            self.v_fuel -= 1
            self.fuel_valor.update(str(self.v_fuel))

    def update(self):
        self.input()
        self.move()
        self.limit()
        self.animation(8, 2, "assets/nave1/nave10"+str(self.frame)+".png")
        self.demage.draw()
        self.demage_valor.draw()
        self.fuel.draw()
        self.fuel_valor.draw()

class Shot(Obj):

   def __init__(self, img, pos, *groups):
       super().__init__(img, pos, *groups)

       self.speed = 5

   def update(self):
       self.rect.y -= self.speed

       if self.rect.y < -100:
           self.kill()