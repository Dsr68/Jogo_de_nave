from scripts.obj.obj import Obj
from scripts.settings import HEIGHT


class Enemy(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 1
        self.life = 1
    
    def destruction(self):
        if self.life <= 0:
            self.kill()
    
    def limits(self):
        if self.rect.y > HEIGHT + self.image.get_height():
            self.kill()

    def move(self):

        self.rect.x += self.speed
        self.rect.y += self.speed

    def update(self):
        self.destruction()
        self.limits()
        self.move()