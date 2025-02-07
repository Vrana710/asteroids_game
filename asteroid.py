import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        # Create a rect for the asteroid for collision detection and drawing
        self.rect = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2,
                                self.radius * 2)
        self.velocity = velocity

    def draw(self, screen):
        # Draw the asteroid as a circle
        # pygame.draw.circle(screen, "white", self.position, self.radius)
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        # Update the asteroid's position or other behavior
        self.rect.center = self.position

    def split(self):
        # Immediately kill the current asteroid
        self.kill()

        # If the asteroid is small enough, do not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Rotate the asteroid's velocity by the random angle in both directions
        velocity_1 = self.velocity.rotate(random_angle)
        velocity_2 = self.velocity.rotate(-random_angle)

        # New smaller radius for the split asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids at the same position but with different velocities
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, velocity_1 * 1.2)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, velocity_2 * 1.2)

        # Add the new asteroids to the asteroid group
        Asteroid.containers[0].add(asteroid_1)
        Asteroid.containers[0].add(asteroid_2)
