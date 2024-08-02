from scripts.obj.asteroide import Asteroide
from scripts.obj.obj import Obj


class BG4(Obj):
    
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)

        self.group = groups

    def draw(self):

        Asteroide("assets/asteroides/asteroide.png", [900, 200], self.group)
        Asteroide("assets/asteroides/asteroide1.png", [990, 360], self.group)
        Asteroide("assets/asteroides/asteroide1.png", [1060, 480], self.group)
        Asteroide("assets/asteroides/asteroide1.png", [100, 500], self.group)