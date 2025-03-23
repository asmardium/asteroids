import pygame # type: ignore
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):

    def ___init__(self, x, y, radius):
        Shot.containers = (shots, updatable, drawable)   #add asteroids to asteroids, drawable, and updatable containers
        super().__init__(x, y, radius)
        #inherits self.position
        #inherits self.velocity
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        #pygame.draw.circle(screen object, color, center point, radius, line width)
        pygame.draw.circle(screen,"white",self.position,self.radius,SHOT_RADIUS) 

    def update(self, dt):
        self.position += (self.velocity * dt)
