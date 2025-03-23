import pygame # type: ignore
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def ___init__(self, x, y, radius):
        Asteroid.containers = (asteroids, updatable, drawable)   #add asteroids to asteroids, drawable, and updatable containers
        super().__init__(x, y, radius)
        #inherits self.position
        #inherits self.velocity
        #inherits self.radius

    def draw(self, screen):
        #pygame.draw.circle(screen object, color, center point, radius, line width)
        pygame.draw.circle(screen,"white",self.position,self.radius,2) 

    def update(self, dt):
        self.position += (self.velocity * dt)
