from Drawable import Drawable #import abstract base class
import pygame

class Text(Drawable):
    color = 0,0,0 #textcolor
    
    def __init__(self, position, text="", visible=True, font=None):
        self.position = position #text position
        self.visible = visible #text visibility
        self.text = text #text
        if not font:
            self.font = pygame.font.SysFont("", 50) #create pygame font (fontName, size)
        else:
            self.font = font

    def draw(self, surface):
        #display text if self.visible
        if self.visible:
            #render the text: font.render(text, antialias, color)
            render = self.font.render(self.text, True, self.color)
            #blit the text on the screen
            surface.blit(render, self.position)

    def get_rect(self):
        #calculate the rect and return it
        return pygame.Rect(self.position,
                           self.font.size(self.text))
