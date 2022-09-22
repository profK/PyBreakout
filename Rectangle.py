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
        #self.rectShape = pymunk.Segment(self.rectBody, (-size[0]/2, size[1]/2), (size[0]/2, size[1]/2), size[1])
        self.rectShape = pymunk.Poly.create_box(self.rectBody,size)
        self.rectShape.mass = 3  # 4
        self.rectShape.friction = 0
        self.rectShape.elasticity = 1
        space.add(self.rectBody, self.rectShape)

    def draw(self,screen) :
        vertices: list = self.rectShape.get_vertices()
        size: tuple = vertices[1]-vertices[3]
        pos: tuple = self.rectBody.position;
        screen.draw.rect(Rect(pos-(size/2),size),(255, 255, 255))