import pygame
from view.obj import Obj
from view.config import HEIGHT, WIDTH


class SpaceShip(Obj):

    def __init__(self, img, pos, *group) -> None:
        super().__init__(img, pos, *group)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.level = 1
        self.life = 3
        self.shots = pygame.sprite.Group()
        self.ticks = 0

    def input(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction.y = -1
        elif key[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        if key[pygame.K_SPACE]:
            self.ticks += 1
            if self.ticks > 30:
                self.ticks = 0
                sound = pygame.mixer.Sound("assets/sounds/shot.ogg")
                sound.play()
                if self.level == 1:
                    Shot("assets/tiros/tiro1.png",[self.rect.x + 30, self.rect.y - 20],[self.shots])
                elif self.level == 2:
                    Shot("assets/tiros/tiro2.png",[self.rect.x + 30, self.rect.y - 20],[self.shots])
                elif self.level == 3:
                    Shot("assets/tiros/tiro3.png",[self.rect.x + 30, self.rect.y - 20],[self.shots])
                elif self.level == 4:
                    Shot("assets/tiros/tiro1.png",[self.rect.x, self.rect.y - 20],[self.shots])
                    Shot("assets/tiros/tiro1.png",[self.rect.x + 60, self.rect.y - 20],[self.shots])
                elif self.level == 5:
                    Shot("assets/tiros/tiro2.png",[self.rect.x, self.rect.y - 20],[self.shots])
                    Shot("assets/tiros/tiro2.png",[self.rect.x + 60, self.rect.y - 20],[self.shots])
                elif self.level == 6:
                    Shot("assets/tiros/tiro3.png",[self.rect.x, self.rect.y - 20],[self.shots])
                    Shot("assets/tiros/tiro3.png",[self.rect.x + 60, self.rect.y - 20],[self.shots])
                else:
                    Shot("assets/tiros/tiro2.png",[self.rect.x, self.rect.y - 20],[self.shots])
                    Shot("assets/tiros/tiro2.png",[self.rect.x + 20, self.rect.y - 20],[self.shots])
                    Shot("assets/tiros/tiro2.png",[self.rect.x + 40, self.rect.y - 20],[self.shots])
                    Shot("assets/tiros/tiro2.png",[self.rect.x + 60, self.rect.y - 20],[self.shots])

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
        self.animation(8,3,"assets/nave/nave")
        #self.input()
        self.limit()
        self.move()