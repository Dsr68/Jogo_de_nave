import pygame
class Obj(pygame.sprite.Sprite):

    def __init__(self, img, pos, *groups) -> None:
        super().__init__(*groups)

        
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = pos)
        self.frame = 0

        self.frame_up = 0
        self.frame_left = 2
        self.frame_right = 4
        self.frame_down = 6
        
        self.tick = 0
    
    def animation(self, speed, n_img, path):
        self.tick += 10
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % n_img
            self.image = pygame.image.load(path+ str(self.frame) + ".png")

    def animation_square(self, path):
        self.image = pygame.image.load(path)
    
    def up(self, speed, path):
        
        self.tick += 10
        if self.tick > speed:
            self.tick = 0
            self.frame_up = (self.frame_up + 1) % 2
            self.image = pygame.image.load(path+ str(self.frame_up) + ".png")
    
    def left(self, speed, path):
        
        self.tick += 10
        if self.tick > speed:
            if self.frame_left == 2:
                self.frame_left += 1
            elif self.frame_left == 3:
                self.frame_left -= 1
            self.tick = 0
            self.frame_left = int((self.frame_left + 3) / 2)
            self.image = pygame.image.load(path+ str(self.frame_left) + ".png")

    def rigth(self, speed, path):
        
        self.tick += 10
        if self.tick > speed:
            if self.frame_right == 4:
                self.frame_right += 1
            elif self.frame_right == 5:
                self.frame_right -= 1
            self.tick = 0
            self.frame_right = int((self.frame_right + 5) / 2)
            self.image = pygame.image.load(path+ str(self.frame_right) + ".png")

    def down(self, speed, path):
        
        if self.tick > speed:
            self.image = pygame.image.load(path + str(self.frame_down) + ".png")
    
    def view_radar(self, path):
        self.image = pygame.image.load(path)