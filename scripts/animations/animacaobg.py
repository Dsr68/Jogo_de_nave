import pygame
from scripts.obj.obj import Obj
from scripts.settings import HEIGHT

class AnimacaoBG:

    def __init__(self, img, pos1, pos2, group):
        self.bg = Obj(img, pos1, group)
        self.bg2 = Obj(img, pos2, group)
        self.group = group

    def draw_radar(self):
        self.radar = Obj("assets/radar.png", [1024, 436], self.group)

    def update(self):

        self.bg.rect.y += 1
        self.bg2.rect.y += 1

        if self.bg.rect.y > HEIGHT:
            self.bg.rect.y = 0
        elif self.bg2.rect.y == 0:
            self.bg2.rect.y = -HEIGHT

