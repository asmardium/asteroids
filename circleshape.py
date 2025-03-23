import pygame # type: ignore
import sys

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self,other_CircleShape):
        distance_to_object = self.position.distance_to(other_CircleShape.position)
        collision_distance = self.radius + other_CircleShape.radius
        if distance_to_object <= (collision_distance):
            print("Game over!")
            sys.exit()

