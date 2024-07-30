from scripts.obj.asteroide import Asteroide
from scripts.obj.obj import Obj

class BG1(Obj):
    
    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)
        
        Asteroide("assets/asteroides/asteroide.png", [300, 500], groups)
        Asteroide("assets/asteroides/asteroide1.png", [160, 460], groups)
        Asteroide("assets/asteroides/asteroide1.png", [360, 280], groups)
        Asteroide("assets/asteroides/asteroide1.png", [200, 300], groups)

        

    