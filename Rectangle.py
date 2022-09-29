import pymunk
from pygame import Rect


class Rectangle :
    def __init__(self,space,position:tuple,size:tuple,  isStatic: bool):
        if isStatic :
            self.rectBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        else :
            self.rectBody = pymunk.Body()
        self.rectShape = pymunk.Poly.create_box( \
            self.rectBody, size)
        self.rectBody.position = position
        self.rectShape.mass = 3
        self.rectShape.friction = 0
        self.rectShape.elasticity = 1
        self.rectShape.rectangle = self; # dynamic object trick
        space.add(self.rectBody,self.rectShape)

    def draw(self,screen):
        vertices: list = self.rectShape.get_vertices()
        size: int = vertices[1] - vertices[3]
        pos: int = self.rectBody.position
        screen.draw.rect(Rect(pos-(size/2),size),(255,255,255))

    def setCollisionType(self,collisionType: int) :
        self.rectShape.collision_type = collisionType
