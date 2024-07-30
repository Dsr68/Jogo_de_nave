from scripts.obj.asteroide import Asteroide
from scripts.obj.obj import Obj


class BG3(Obj):
    
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)
        
        Asteroide("assets/asteroides/asteroide.png", [600, 200], groups)
        Asteroide("assets/asteroides/asteroide1.png", [660, 360], groups)
        Asteroide("assets/asteroides/asteroide1.png", [760, 480], groups)
        Asteroide("assets/asteroides/asteroide1.png", [700, 500], groups)