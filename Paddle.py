from Rectangle import Rectangle
from pymunk import space

class Paddle(Rectangle) :
    def __init__(self,space, position:tuple, size:tuple) :
        super().__init__(space, position,size,True) # we will move but we dont want physics to

    def move(self,myspace: space,deltaX:int, deltaY:int) :
        position: tuple = self.rectBody.position
        position = position + (deltaX,deltaY)
        self.rectBody.position = position
        myspace.reindex_shape(self.rectShape)
