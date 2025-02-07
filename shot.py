import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        # Initialize as a CircleShape but with velocity for shots
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        # Create a rect for the shot for collision detection and drawing
        self.rect = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, "yellow", self.position, self.radius)

    def update(self, dt):
        # Update the shot position
        self.position += self.velocity * dt

        # Update the rect position based on the shot's current position
        self.rect.center = self.position
