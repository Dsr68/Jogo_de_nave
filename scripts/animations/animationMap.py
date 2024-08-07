from scripts.bases.obj import Obj
from scripts.settings import HEIGHT, WIDTH


class AnimationMap:

    def __init__(self, img, group) -> None:
        
        self.bg1 = Obj(img, [0, 0], group)
        self.bg2 = Obj(img, [-WIDTH, 0], group)
        self.bg3 = Obj(img, [-WIDTH, -HEIGHT], group)
        self.bg4 = Obj(img, [0, -HEIGHT], group)
    
    def update_up(self):

        if self.bg3.rect.y < 0 and self.bg4.rect.y < 0:
            self.bg1.rect.y += 1
            self.bg2.rect.y += 1
            self.bg3.rect.y += 1
            self.bg4.rect.y += 1
    