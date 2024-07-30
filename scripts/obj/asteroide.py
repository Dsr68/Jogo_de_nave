
from scripts.obj.obj import Obj

class Asteroide(Obj):

    def __init__(self, img, pos, *groups) -> None:
        super().__init__(img, pos, *groups)
        
