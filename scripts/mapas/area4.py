from scripts.obj.asteroide import Asteroide
from scripts.obj.obj import Obj


class BG4(Obj):
    
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)
        
        Asteroide("assets/asteroides/asteroide.png", [900, 200], groups)
        Asteroide("assets/asteroides/asteroide1.png", [990, 360], groups)
        Asteroide("assets/asteroides/asteroide1.png", [1060, 480], groups)
        Asteroide("assets/asteroides/asteroide1.png", [100, 500], groups)