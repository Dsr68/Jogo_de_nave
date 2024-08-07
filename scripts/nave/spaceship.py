import pygame

from scripts.bases.obj import Obj
from scripts.settings import HEIGHT, WIDTH
from scripts.text import Text


class Spaceship(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.life = 3
        self.side = "up"

        self.tiros = pygame.sprite.Group()
        self.ticks = 0

        self.v_demange = 100
        self.format_demage = str(self.v_demange)
        self.demage = Text("assets/fonts/airstrike.ttf", 25, "Damage", "white", [30, 30])
        self.demage_valor = Text("assets/fonts/airstrike.ttf", 25, self.format_demage + "%", "white", [160, 30])

        self.v_fuel = 100.00
        self.format_fuel = "{:.2f}".format(self.v_fuel)
        self.fuel = Text("assets/fonts/airstrike.ttf", 25, "Fuel", "white", [30, 60])
        self.fuel_valor = Text("assets/fonts/airstrike.ttf", 25, self.format_fuel, "white", [160, 60])

    def input(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction.y = -1
            self.animation(8, 2, "assets/nave1/up/nave10"+str(self.frame)+".png")
            self.side = "up"
            self.cosume()    
        elif key[pygame.K_s]:
            self.direction.y = 1
            self.image = pygame.image.load("assets/nave1/down/nave100.png")
            self.side = "down"
            self.cosume()
        else:
            self.direction.y = 0

        if key[pygame.K_a] :
            self.direction.x = -1
            if key[pygame.K_a] != key[pygame.K_w] and key[pygame.K_a] != key[pygame.K_s]:
                self.animation(8, 2, "assets/nave1/left/nave10"+str(self.frame)+".png")
                self.side = "left"
            self.cosume()
        elif key[pygame.K_d]:
            self.direction.x = 1
            if key[pygame.K_d] != key[pygame.K_w] and key[pygame.K_d] != key[pygame.K_s]:
                self.animation(8, 2, "assets/nave1/rigth/nave10"+str(self.frame)+".png")
                self.side = "rigth"
            self.cosume()
        else:
            self.direction.x = 0

        click = pygame.mouse.get_pressed()

        if click[0] == True:
            self.ticks += 1
            
            if self.ticks == 1:
                self.position_shot()

            elif self.ticks > 30:
                self.position_shot()
                self.ticks = 0
                

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
            self.v_fuel -= 0.01
            self.fuel_valor.update(str(round(self.v_fuel, 2)))

    def position_shot(self):

        if self.side == "up":
            Shot_vertical_up("assets/tiro1/tiro1.png", [self.rect.x, self.rect.y-20], self.tiros)
        elif self.side == "down":
            Shot_vertical_down("assets/tiro1/tiro1.png", [self.rect.x, self.rect.y+20], self.tiros)
        elif self.side == "left":
            Shot_horizontal_left("assets/tiro1/tiro2.png", [self.rect.x-20, self.rect.y], self.tiros)
        elif self.side == "rigth":
            Shot_horizontal_rigth("assets/tiro1/tiro2.png", [self.rect.x+20, self.rect.y], self.tiros)

    def update(self):
        self.input()
        self.move()
        self.limit()
        self.demage.draw()
        self.demage_valor.draw()
        self.fuel.draw()
        self.fuel_valor.draw()

class Shot_vertical_up(Obj):

   def __init__(self, img, pos, *groups):
       super().__init__(img, pos, *groups)

       self.speed = 20

   def update(self):
       self.rect.y -= self.speed

       if self.rect.y < 0:
           self.kill()

class Shot_vertical_down(Obj):

   def __init__(self, img, pos, *groups):
       super().__init__(img, pos, *groups)

       self.speed = 20

   def update(self):
       self.rect.y += self.speed

       if self.rect.y > HEIGHT:
           self.kill()

class Shot_horizontal_left(Obj):

   def __init__(self, img, pos, *groups):
       super().__init__(img, pos, *groups)

       self.speed = 20

   def update(self):
       self.rect.x -= self.speed

       if self.rect.x < 0:
           self.kill()

class Shot_horizontal_rigth(Obj):

   def __init__(self, img, pos, *groups):
       super().__init__(img, pos, *groups)

       self.speed = 20

   def update(self):
       self.rect.x += self.speed

       if self.rect.x > WIDTH:
           self.kill()