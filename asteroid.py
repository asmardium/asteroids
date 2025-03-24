import pygame # type: ignore
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):

    def ___init__(self, x, y, radius, manager):
        #add asteroids to asteroids, drawable, and updatable pygame groups on object creation
        Asteroid.containers = (asteroids, updatable, drawable)  #these are defined in main.py
        super().__init__(x, y, radius)
        #inherits self.position
        #inherits self.velocity
        #inherits self.radius
        self.manager = manager

    def draw(self, screen):
        #pygame.draw.circle(screen object, color, center point, radius, line width)
        pygame.draw.circle(screen,"white",self.position,self.radius,2) 

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):       
        self.kill()
        #check whether to create more asteroids; if False, return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #generate angle to randomize new asteroid directions
        random_angle = random.uniform(20,50)
        #calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #generate velocity vectors
        new_position_1 = pygame.Vector2(self.position[0], self.position[1])
        new_velocity_1 = self.velocity.rotate(-random_angle) * 1.2
        new_position_2 = pygame.Vector2(self.position[0], self.position[1])
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2
        #create new asteroids and assign updated random velocity
        # (self, radius, position, velocity):
        self.manager.spawn(new_radius, new_position_1, new_velocity_1)
        self.manager.spawn(new_radius, new_position_2, new_velocity_2)





