import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Create a rect for the asteroid for collision detection and drawing
        self.rect = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2,
                                self.radius * 2)

    def draw(self, screen):
        # Draw the asteroid as a circle
        # pygame.draw.circle(screen, "white", self.position, self.radius)
        pygame.draw.circle(screen, "gray", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        # Update the asteroid's position or other behavior
        self.rect.center = self.position
