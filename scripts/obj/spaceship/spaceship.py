import pygame
from scripts.obj.spaceship.front import Shot_h_left, Shot_h_rigth, Shot_v_down, Shot_v_up
from scripts.obj.obj import Obj
from scripts.settings import HEIGHT, WIDTH


class SpaceShip(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.frame = 0
        self.level = 1
        self.damage = 100
        
        self.shots = pygame.sprite.Group()
        self.direction_shot = "up"
            
        self.ticks = 0

    def input(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction.y = -1
            self.up(30,"assets/nave1/nave10")
            self.direction_shot = "up"
        elif key[pygame.K_s]:
            self.direction.y = 1
            self.down(30, "assets/nave1/nave10")
            self.direction_shot = "down"
        else:
            self.direction.y = 0
        
        if key[pygame.K_a]:
            self.direction.x = -1
            self.left(30, "assets/nave1/nave10")
            self.direction_shot = "left"
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.rigth(30, "assets/nave1/nave10")
            self.direction_shot = "rigth"
        else:
            self.direction.x = 0
        event = pygame.mouse.get_pressed()
        if event[0] == True:
            self.ticks += 1
            if self.ticks > 5:
                self.ticks = 0
                sound = pygame.mixer.Sound("assets/sounds/shot.ogg")
                sound.play()
                
                if self.direction_shot == "up":
                    Shot_v_up("assets/tiro1/tiro1.png", [self.rect.x + 1, self.rect.y - 20],[self.shots])
                if self.direction_shot == "left":
                    Shot_h_left("assets/tiro1/tiro2.png", [self.rect.x - 20, self.rect.y - 1],[self.shots])
                if self.direction_shot == "rigth":
                    Shot_h_rigth("assets/tiro1/tiro2.png", [self.rect.x + 20, self.rect.y - 1],[self.shots])
                if self.direction_shot == "down":
                    Shot_v_down("assets/tiro1/tiro1.png", [self.rect.x + 1, self.rect.y + 20],[self.shots])

    def limit(self):

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.image.get_width():
            self.rect.x  = WIDTH - self.image.get_width()
        
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.image.get_height():
            self.rect.y  = HEIGHT - self.image.get_height()

    def move(self):

        self.rect.center += self.direction * self.speed
        
    
    def update(self):
        self.input()
        self.limit()
        self.move()
    