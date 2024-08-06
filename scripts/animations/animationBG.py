from scripts.bases.obj import Obj
from scripts.settings import HEIGHT


class AnimationMenu:

    def __init__(self, img, pos1, pos2, group) -> None:
        
        self.bg1 = Obj(img, pos1, group)
        self.bg2 = Obj(img, pos2, group)
    
    def update(self):

        self.bg1.rect.y += 1
        self.bg2.rect.y += 1

        if self.bg1.rect.y > HEIGHT:
            self.bg1.rect.y = 0
        elif self.bg2.rect.y == 0:
            self.bg2.rect.y = -HEIGHT

    