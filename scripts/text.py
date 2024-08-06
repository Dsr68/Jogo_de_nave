import pygame

class Text:

    def __init__(self, font, size, text, color, pos) -> None:

        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color).convert_alpha()
        self.color = color
        self.position = pos
        self.text_alpha = 255
        self.speed = 5

    def draw(self):
        self.display.blit(self.text, self.position)

    def draw_fade(self):

        if self.text_alpha > 0:
            self.text_alpha -= self.speed
        else:
            self.text_alpha = 255

        self.text.set_alpha(self.text_alpha)
        self.display.blit(self.text, self.position)

    def update(self, text):
        self.text = self.font.render(text, True, self.color).convert_alpha()
        