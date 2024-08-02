from scripts.mapas.area1 import BG1
from scripts.obj.spaceship.spaceship import SpaceShip
from scripts.scene.scene import Scene
from scripts.settings import HEIGHT, WIDTH

class BG(Scene):
    
    def __init__(self, background) -> None:
        super().__init__()

        self.area = "area1"
        self.img = "assets/menu/espaco.png"
        self.pos = [0, 0]
        
        self.bg = background
        self.spaceship = SpaceShip("assets/nave1/nave100.png", [600, 600], self.all_sprites)

    def change_background(self, background):
        self.bg = background
            
       
    def update(self):
        self.draw()
        self.spaceship.update()
    
        
        


