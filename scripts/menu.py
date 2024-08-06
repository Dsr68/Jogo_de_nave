import pygame
from scripts.animations.animationBG import AnimationMenu
from scripts.bases.obj import Obj
from scripts.bases.scene import Scene
from scripts.text import Text
from scripts.settings import *

class Menu(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimationMenu("assets/menu/espaco.png", [0, 0], [0, -720], self.all_sprites)
        self.title = Text("assets/fonts/airstrike.ttf", 50, "Spaceship 13K", "White", [450, 300])
        self.text_info = Text("assets/fonts/airstrike.ttf", 21, "Press Start to Play", "White", [508, 513])

    def events(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
        
    def update(self):
        self.bg.update()
        self.title.draw()
        self.text_info.draw_fade()

        return super().update()
    