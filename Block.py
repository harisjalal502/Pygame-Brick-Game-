#BLOCK CLASS

from Drawable import Drawable #import base class
import pygame

class Block(Drawable):
    size = [20,20] #block size [width, height]
    linewidth = 1 #outline width of the block

    def __init__(self, position, visible=True):
        self.position = position #block position
        self.visible = visible #block visibility
        self.rect = pygame.Rect(self.position, self.size) #calculating block rect

    def draw(self, surface):
        #draw block if visible
        if self.visible:
            #draw block: pygame.draw.rect(surface, color, rect)
            #rect: (xpos, ypos, width, height)
            pygame.draw.rect(surface, (0,0,255), self.rect)
            #draw block outline
            pygame.draw.rect(surface, (0,0,0),   self.rect, self.linewidth)

    def get_rect(self):
        return self.rect #return the rect
