import pygame
from scripts.asteroide import Asteroide
from scripts.bases.obj import Obj
from scripts.settings import HEIGHT, WIDTH


class AnimationMap:

    def __init__(self, img, group) -> None:

        self.areas = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()
        self.estacoes = pygame.sprite.Group()

        self.area1 = Obj("assets/menu/espaco.png", [0, 0], [self.areas,  group])
        self.asteroide1 = Asteroide("assets/asteroides/asteroide.png", [50, 600], [self.asteroides, group])
        self.asteroide3 = Asteroide("assets/asteroides/asteroide.png", [250, 600], [self.asteroides, group])
        self.asteroide4 = Asteroide("assets/asteroides/asteroide.png", [1100, 60], [self.asteroides, group])
        self.asteroide5 = Asteroide("assets/asteroides/asteroide3.png", [60, 60], [self.asteroides, group])
        self.asteroide6 = Asteroide("assets/asteroides/asteroide1.png", [650, 320], [self.asteroides, group])
        self.estacao = Asteroide("assets/estacao.png", [850, 300], [self.estacoes, group])

        self.area2 = Asteroide("assets/menu/espaco.png", [-1280, 0], [self.areas, group])
        self.area3 = Asteroide("assets/menu/espaco.png", [-2560, 0], [self.areas, group])
        
        self.area4 = Asteroide("assets/menu/espaco.png", [-3840, 0], [self.areas, group])
        self.asteroide7 = Asteroide("assets/asteroides/asteroide.png", [-3790, 600], [self.asteroides, group])
        self.asteroide8 = Asteroide("assets/asteroides/asteroide.png", [-3590, 600], [self.asteroides, group])
        self.asteroide9 = Asteroide("assets/asteroides/asteroide.png", [-2740, 60], [self.asteroides, group])
        self.asteroide10 = Asteroide("assets/asteroides/asteroide3.png", [-3790, 60], [self.asteroides, group])
        self.asteroide11 = Asteroide("assets/asteroides/asteroide1.png", [-3190, 320], [self.asteroides, group])
        self.estacao = Asteroide("assets/estacao.png", [-3790, 200], [self.estacoes, group])

        self.area5 = Asteroide("assets/menu/espaco.png", [0, -720], [self.areas, group])
        self.area6 = Asteroide("assets/menu/espaco.png", [-1280, -720], [self.areas, group])
        self.area7 = Asteroide("assets/menu/espaco.png", [-2560, -720], [self.areas, group])
        self.area8 = Asteroide("assets/menu/espaco.png", [-3840, -720], [self.areas, group])

        self.area9 = Asteroide("assets/menu/espaco.png", [0, -1440], [self.areas, group])
        self.area10 = Asteroide("assets/menu/espaco.png", [-1280, -1440], [self.areas, group])
        self.area11 = Asteroide("assets/menu/espaco.png", [-2560, -1440], [self.areas, group])
        self.area12 = Asteroide("assets/menu/espaco.png", [-3840, -1440], [self.areas, group])

        self.area13 = Asteroide("assets/menu/espaco.png", [0, -2160], [self.areas, group])
        
        self.area14 = Asteroide("assets/menu/espaco.png", [-1280, -2160], [self.areas, group])
        self.asteroide7 = Asteroide("assets/asteroides/asteroide.png", [50, -1560], [self.asteroides, group])
        self.asteroide8 = Asteroide("assets/asteroides/asteroide.png", [250, -1560], [self.asteroides, group])
        self.asteroide9 = Asteroide("assets/asteroides/asteroide.png", [1100, -2100], [self.asteroides, group])
        self.asteroide10 = Asteroide("assets/asteroides/asteroide3.png", [60, -2100], [self.asteroides, group])
        self.asteroide11 = Asteroide("assets/asteroides/asteroide1.png", [650, -1840], [self.asteroides, group])
        self.estacao = Asteroide("assets/estacao.png", [800, -1800], [self.estacoes, group])
        
        self.area15 = Asteroide("assets/menu/espaco.png", [-2560, -2160], [self.areas, group])
        
        self.area16 = Asteroide("assets/menu/espaco.png", [-3840, -2160], [self.areas, group])
        self.asteroide7 = Asteroide("assets/asteroides/asteroide.png", [-3790, -1560], [self.asteroides, group])
        self.asteroide8 = Asteroide("assets/asteroides/asteroide.png", [-3590, -1560], [self.asteroides, group])
        self.asteroide9 = Asteroide("assets/asteroides/asteroide.png", [-2740, -2100], [self.asteroides, group])
        self.asteroide10 = Asteroide("assets/asteroides/asteroide3.png", [-2500, -2100], [self.asteroides, group])
        self.asteroide11 = Asteroide("assets/asteroides/asteroide1.png", [-3190, -1840], [self.asteroides, group])
        self.estacao = Asteroide("assets/estacao.png", [-3790, -1940], [self.estacoes, group])
           
    
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
            
     
            