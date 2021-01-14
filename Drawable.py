#abstract Drawable base class

#import required modules for creating abstract classes and methods
from abc import ABCMeta, abstractmethod

class Drawable(metaclass=ABCMeta):
    position = [0,0] #position
    visible = True #visibility

    #making this an abstract method
    #this class cannot be created without overwriting the functions
    #draw and get_rect in the class that inherits from the Drawable class
    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def get_rect(self):
        pass
