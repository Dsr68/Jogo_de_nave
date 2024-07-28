
from scripts.groups import Enemy


class Resource(Enemy):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 2
    
    def update(self):
        self.animation(16,3,"assets/nave/powerup")
        return super().update()