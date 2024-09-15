import pygame
from scripts.bases.obj import Obj

class Asteroide(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        quantidade = 100
        coletado = False
        