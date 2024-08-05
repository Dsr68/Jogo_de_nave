import pygame

class Obj:

    def __init__(self, img, pos, *group) -> None:
        
        self.surface = pygame.display.get_surface()
        self.image = pygame.image.load(img)
        self.pos = pos
        self.group = group

    def draw(self):
        self.surface.blit(self.image, self.pos)

    def update(self):
        pass