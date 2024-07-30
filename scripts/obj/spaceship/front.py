from scripts.obj.obj import Obj


class Shot_v_up(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 15
    
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y < -100:
            self.kill()

class Shot_v_down(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 15
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.y < -100:
            self.kill()

class Shot_h_left(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 15
    
    def update(self):
        self.rect.x -= self.speed

        if self.rect.x < -100:
            self.kill()


class Shot_h_rigth(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 15
    
    def update(self):
        self.rect.x += self.speed

        if self.rect.x < 100:
            self.kill()