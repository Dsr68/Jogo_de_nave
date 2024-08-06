from scripts.bases.obj import Obj
from scripts.settings import HEIGHT


class Enemy(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 5
        self.life = 3
    
    def destruction(self):

        if self.life == 0:
            self.kill()

    def move(self):
        self.rect.y += self.speed

    def limit(self):
        
        if self.rect.y > HEIGHT + self.image.get_height():
            self.kill()

    def update(self):
        
        self.move()
        self.limit()
        self.destruction()
