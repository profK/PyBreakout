import pymunk

class Circle :
    def __init__(self,space,position:tuple, diameter:float) :
        self.circleBody = pymunk.Body()
        self.circleBody.position = position
        self.circleShape = pymunk.Circle(self.circleBody,diameter)
        self.circleShape.mass = 3
        self.circleShape.friction = 0
        self.circleShape.elasticity = 1
        space.add(self.circleBody, self.circleShape)

    def draw(self,screen) :
        screen.draw.circle(self.circleBody.position,
                           self.circleShape.radius, (255,255,255))

    def setCollisionType(self, collisionType: int):
        self.circleShape.collision_type = collisionType