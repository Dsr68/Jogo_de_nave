import pygame
from scripts.bases.obj import Obj
from scripts.settings import HEIGHT, WIDTH


class AnimationMap:

    def __init__(self, img, group) -> None:

        self.areas = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()
        self.estacoes = pygame.sprite.Group()

        self.area1 = Obj("assets/menu/espaco.png", [0, 0], [self.areas,  group])
        self.asteroide1 = Obj("assets/asteroides/asteroide.png", [50, 600], [self.asteroides, group])
        self.asteroide3 = Obj("assets/asteroides/asteroide.png", [250, 600], [self.asteroides, group])
        self.asteroide4 = Obj("assets/asteroides/asteroide.png", [1100, 60], [self.asteroides, group])
        self.asteroide5 = Obj("assets/asteroides/asteroide3.png", [60, 60], [self.asteroides, group])
        self.asteroide6 = Obj("assets/asteroides/asteroide1.png", [650, 320], [self.asteroides, group])
        self.estacao = Obj("assets/estacao.png", [850, 300], [self.estacoes, group])

        self.area2 = Obj("assets/menu/espaco.png", [-1280, 0], [self.areas, group])
        self.area3 = Obj("assets/menu/espaco.png", [-2560, 0], [self.areas, group])
        
        self.area4 = Obj("assets/menu/espaco.png", [-3840, 0], [self.areas, group])
        self.asteroide7 = Obj("assets/asteroides/asteroide.png", [-3790, 600], [self.asteroides, group])
        self.asteroide8 = Obj("assets/asteroides/asteroide.png", [-3590, 600], [self.asteroides, group])
        self.asteroide9 = Obj("assets/asteroides/asteroide.png", [-2740, 60], [self.asteroides, group])
        self.asteroide10 = Obj("assets/asteroides/asteroide3.png", [-3790, 60], [self.asteroides, group])
        self.asteroide11 = Obj("assets/asteroides/asteroide1.png", [-3190, 320], [self.asteroides, group])
        self.estacao = Obj("assets/estacao.png", [-3790, 200], [self.estacoes, group])

        self.area5 = Obj("assets/menu/espaco.png", [0, -720], [self.areas, group])
        self.area6 = Obj("assets/menu/espaco.png", [-1280, -720], [self.areas, group])
        self.area7 = Obj("assets/menu/espaco.png", [-2560, -720], [self.areas, group])
        self.area8 = Obj("assets/menu/espaco.png", [-3840, -720], [self.areas, group])

        self.area9 = Obj("assets/menu/espaco.png", [0, -1440], [self.areas, group])
        self.area10 = Obj("assets/menu/espaco.png", [-1280, -1440], [self.areas, group])
        self.area11 = Obj("assets/menu/espaco.png", [-2560, -1440], [self.areas, group])
        self.area12 = Obj("assets/menu/espaco.png", [-3840, -1440], [self.areas, group])

        self.area13 = Obj("assets/menu/espaco.png", [0, -2160], [self.areas, group])
        
        self.area14 = Obj("assets/menu/espaco.png", [-1280, -2160], [self.areas, group])
        self.asteroide7 = Obj("assets/asteroides/asteroide.png", [50, -1560], [self.asteroides, group])
        self.asteroide8 = Obj("assets/asteroides/asteroide.png", [250, -1560], [self.asteroides, group])
        self.asteroide9 = Obj("assets/asteroides/asteroide.png", [1100, -2100], [self.asteroides, group])
        self.asteroide10 = Obj("assets/asteroides/asteroide3.png", [60, -2100], [self.asteroides, group])
        self.asteroide11 = Obj("assets/asteroides/asteroide1.png", [650, -1840], [self.asteroides, group])
        self.estacao = Obj("assets/estacao.png", [800, -1800], [self.estacoes, group])
        
        self.area15 = Obj("assets/menu/espaco.png", [-2560, -2160], [self.areas, group])
        
        self.area16 = Obj("assets/menu/espaco.png", [-3840, -2160], [self.areas, group])
        self.asteroide7 = Obj("assets/asteroides/asteroide.png", [-3790, -1560], [self.asteroides, group])
        self.asteroide8 = Obj("assets/asteroides/asteroide.png", [-3590, -1560], [self.asteroides, group])
        self.asteroide9 = Obj("assets/asteroides/asteroide.png", [-2740, -2100], [self.asteroides, group])
        self.asteroide10 = Obj("assets/asteroides/asteroide3.png", [-2500, -2100], [self.asteroides, group])
        self.asteroide11 = Obj("assets/asteroides/asteroide1.png", [-3190, -1840], [self.asteroides, group])
        self.estacao = Obj("assets/estacao.png", [-3790, -1940], [self.estacoes, group])
           
    
    def update_up(self):

        if self.area16.rect.y < 0:
            for area in self.areas:  
                area.rect.y += 5
            for asteroide in self.asteroides:
                asteroide.rect.y += 5
            for estacao in self.estacoes:
                estacao.rect.y += 5

    def update_down(self):

        if self.area1.rect.y > 0:
            for area in self.areas:  
                area.rect.y -= 5
            for asteroide in self.asteroides:
                asteroide.rect.y -= 5
            for estacao in self.estacoes:
                estacao.rect.y -= 5
    
    def update_left(self):

        if self.area4.rect.x < 0:
            for area in self.areas:  
                area.rect.x += 5
            for asteroide in self.asteroides:
                asteroide.rect.x += 5
            for estacao in self.estacoes:
                estacao.rect.x += 5

    def update_rigth(self):

        if self.area1.rect.x > 0:
            for area in self.areas:  
                area.rect.x -= 5
            for asteroide in self.asteroides:
                asteroide.rect.x -= 5
            for estacao in self.estacoes:
                estacao.rect.x -= 5
            
     
            