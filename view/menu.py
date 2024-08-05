from view.text import Text
import pygame

from view.obj import Obj

class Menu():

    def __init__(self):
        super().__init__()

        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/menu/espaco.png",[0,0],[self.all_sprites])
        self.title = Text("assets/fonts/airstrike.ttf", 50,"SpaceShip 13k", "white", [448,288])
        self.text_info = Text("assets/fonts/airstrike.ttf", 21,"Press Start To Play", "white", [508,513])

        self.active = True
    
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False

    def draw(self):
        self.bg.draw()

    def update(self):
        
        self.title.draw()
        self.text_info.drawFade()
