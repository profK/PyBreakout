import pymunk
from pygame import Rect

class Rectangle :
    def __init__(self,space,position:tuple, size: tuple,static: bool) :
        # make rectangle physics object
        if (static) :
            self.rectBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        else :
            self.rectBody = pymunk.Body()
        self.rectBody.position = position
        self.rectShape = pymunk.Segment(self.rectBody, (-size[0]/2, -size[1]/2), (size[0]/2, size[1]/2), size[1])
        self.rectShape.mass = 3  # 4
        self.rectShape.friction = 0
        self.rectShape.elasticity = 1
        space.add(self.rectBody, self.rectShape)

    def draw(self,screen) :
        screen.draw.rect(Rect(self.rectBody.position+self.rectShape.a,
                         self.rectShape.b-self.rectShape.a),(255, 255, 255))