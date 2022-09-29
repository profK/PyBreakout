from Rectangle import Rectangle
from pymunk import space

class Paddle(Rectangle) :
    def __init__(self,space,position:tuple,size:tuple) :
        super().__init__(space,position,size,True)

    def move(self,space,deltaX:int, deltaY:int) :
        position: tuple = self.rectBody.position
        position = position + (deltaX,deltaY)
        self.rectBody.position = position
        space.reindex_shape(self.rectShape)