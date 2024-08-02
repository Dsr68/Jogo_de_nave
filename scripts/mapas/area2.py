from scripts.obj.asteroide import Asteroide
from scripts.obj.obj import Obj


class BG2(Obj):
    
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)

        self.group = groups
        
    def draw(self):

            Asteroide("assets/asteroides/asteroide.png", [300, 200], self.group)
            Asteroide("assets/asteroides/asteroide1.png", [160, 360], self.group)
            Asteroide("assets/asteroides/asteroide1.png", [360, 380], self.group)
            Asteroide("assets/asteroides/asteroide1.png", [200, 300], self.group)

        