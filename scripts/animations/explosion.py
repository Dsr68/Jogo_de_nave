from scripts.obj.obj import Obj


class Explosion(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.ticks = 0
    
    def update(self):
        self.animation(5,5,"assets/explosion/")

        self.ticks += 1
        if self.ticks > 25:
            self.kill()
        return super().update()