from scripts.groups.enemys import Enemy

class SmallShip(Enemy):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 6
        self.life = 1
    
    def update(self):
        self.animation(8,3,"assets/nave/enemy")
        return super().update()