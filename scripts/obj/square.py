from scripts.groups import Enemy_square


class Square(Enemy_square):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 4
        self.life = 1
    
    def update(self):
        self.animation_square("assets/square/square0.png")
        return super().update()