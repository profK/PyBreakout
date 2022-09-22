import pymunk
class Circle :
    def __init__(self,space:pymunk.Space, position: tuple, diameter: int) :
        self.circleBody = pymunk.Body()
        self.circleBody.position = position
        self.circleShape = pymunk.Circle(self.circleBody, diameter)  # 3
        self.circleShape.mass = 3  # 4
        self.circleShape.friction = 0
        self.circleShape.elasticity = 0.75;
        space.add(self.circleBody, self.circleShape)

    def draw(self, screen) :
        screen.draw.circle(self.circleBody.position, 20, (255, 255, 255))

