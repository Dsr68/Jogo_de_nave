
class Square():

  def __init__(self, img, pos_obj):
    
        self.speed = 1
        self.life = 1
        self.posX = 0
        self.posY = 0
        self.rect_obj = pos_obj
        self.tick = 0

def position(self):

    if self.rect_obj.x == 0:
        self.posX = 1054
    else:
        self.rect_obj.x = 1054 + int(self.rect_obj.x/1280)
    
    if self.rect_obj.y == -3600:            
        self.posY = 288
    elif self.rect_obj.y > -3600 and self.rect_obj.y < 0:
        self.poxY = 288 + int((self.rect_obj + 3600)/720)
    
    def slow(self):

        self.tick += 1

        if self.tick == 60:
            self.speed = 0
            self.tick = 0
        else:
            self.speed = 1
    
    def debug(self):
        print(str(self.posY))

    def update(self):
        
        self.animation_square("assets/square/square0.png")
        self.slow()
