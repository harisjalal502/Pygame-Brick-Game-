#BALL CLASS

from Drawable import Drawable #import base class
import pygame.gfxdraw #special pygame drawing module

class Ball(Drawable):
    color = 255,0,0 #ball color
    radius = 8 #ball radius

    def __init__(self, position, visible=True):
        self.position = position #ball position
        self.visible = visible #ball visibility

    def draw(self, surface):
        #draw ball if visible
        if self.visible:
            #pygame.gfxdraw.filled_circle(surface, xpos, ypos, radius, color)
            #round positions because a pixel must be an integer
            pygame.gfxdraw.filled_circle(surface, round(self.position[0]), round(self.position[1]), self.radius, self.color)

    def get_rect(self):
        #calculatethe rect for the circle and return it
        return pygame.Rect(self.position[0]-self.radius,
                           self.position[1]-self.radius,
                           self.radius*2,
                           self.radius*2)
