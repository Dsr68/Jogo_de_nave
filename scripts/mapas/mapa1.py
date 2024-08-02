from scripts.mapas.area1 import BG1
<<<<<<< HEAD
=======
from scripts.obj.spaceship.spaceship import SpaceShip
>>>>>>> 7e26cb8 (Primeiro commit desktop)
from scripts.scene.scene import Scene
from scripts.settings import HEIGHT, WIDTH

class BG(Scene):
    
    def __init__(self) -> None:
        super().__init__()

        self.area = "area1"
        self.img = "assets/menu/espaco.png"
        self.pos = [0, 0]
        
        self.bg = BG1(self.img, self.pos, self.all_sprites)
            
       
    def update(self):
        self.draw()
<<<<<<< HEAD
=======

>>>>>>> 7e26cb8 (Primeiro commit desktop)
        
        


