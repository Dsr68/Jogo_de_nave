from scripts.obj.obj import Obj


class Resource(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 1
        self.life = 1

